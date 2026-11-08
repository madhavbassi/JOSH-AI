import { useEffect, useRef } from 'react';
import * as THREE from 'three';

const vertexShader = `
varying vec3 vObjectPosition;
varying vec3 vNormalWorld;
varying vec3 vViewDirection;
varying vec2 vUv;
void main() {
  vec4 worldPosition = modelMatrix * vec4(position, 1.0);
  vObjectPosition = position;
  vNormalWorld = normalize(mat3(modelMatrix) * normal);
  vViewDirection = normalize(cameraPosition - worldPosition.xyz);
  vUv = uv;
  gl_Position = projectionMatrix * viewMatrix * worldPosition;
}`;

const coreShader = `
uniform float uTime;
varying vec3 vObjectPosition;
varying vec3 vNormalWorld;
varying vec3 vViewDirection;
varying vec2 vUv;
float hash31(vec3 p) {
  p = fract(p * 0.1031);
  p += dot(p, p.yzx + 33.33);
  return fract((p.x + p.y) * p.z);
}
float noise3(vec3 p) {
  vec3 i = floor(p), f = fract(p);
  f = f * f * (3.0 - 2.0 * f);
  return mix(mix(mix(hash31(i), hash31(i + vec3(1,0,0)), f.x), mix(hash31(i + vec3(0,1,0)), hash31(i + vec3(1,1,0)), f.x), f.y), mix(mix(hash31(i + vec3(0,0,1)), hash31(i + vec3(1,0,1)), f.x), mix(hash31(i + vec3(0,1,1)), hash31(i + vec3(1,1,1)), f.x), f.y), f.z);
}
float fbm(vec3 p) {
  float n = 0.0;
  n += 0.58 * noise3(p);
  n += 0.27 * noise3(p * 2.07 + 3.1);
  n += 0.15 * noise3(p * 4.13 - 1.7);
  return n;
}
void main() {
  vec3 N = normalize(vNormalWorld);
  vec3 V = normalize(vViewDirection);
  vec3 L = normalize(vec3(-0.56, 0.58, 0.82));
  float grain = fbm(vObjectPosition * 5.8 + vec3(0.0, uTime * 0.008, 0.0));
  float broad = fbm(vObjectPosition * 2.7 + vec3(4.2, 0.0, -2.0));
  float diffuse = max(dot(N, L), 0.0);
  float terminator = smoothstep(-0.48, 0.36, dot(N, L));
  float rim = pow(1.0 - max(dot(N, V), 0.0), 2.8);
  vec3 base = vec3(0.006, 0.012, 0.027);
  vec3 mineral = vec3(0.018, 0.044, 0.088);
  vec3 surface = mix(base, mineral, smoothstep(0.25, 0.78, broad) * 0.68 + grain * 0.11);
  surface *= 0.30 + 0.70 * terminator;
  surface += vec3(0.012, 0.041, 0.092) * diffuse * (0.18 + grain * 0.22);
  surface += vec3(0.008, 0.095, 0.22) * rim * 0.25;
  float highlight = pow(max(dot(reflect(-L, N), V), 0.0), 34.0);
  surface += vec3(0.12, 0.30, 0.56) * highlight * 0.20;
  gl_FragColor = vec4(surface, 1.0);
}`;

const atmosphereVertex = `
varying vec3 vNormalWorld;
varying vec3 vViewDirection;
void main() {
  vec4 worldPosition = modelMatrix * vec4(position, 1.0);
  vNormalWorld = normalize(mat3(modelMatrix) * normal);
  vViewDirection = normalize(cameraPosition - worldPosition.xyz);
  gl_Position = projectionMatrix * viewMatrix * worldPosition;
}`;

const atmosphereFragment = `
uniform vec3 uBlue;
uniform vec3 uCyan;
uniform float uStrength;
uniform float uExponent;
varying vec3 vNormalWorld;
varying vec3 vViewDirection;
void main() {
  float facing = abs(dot(normalize(vNormalWorld), normalize(vViewDirection)));
  float fresnel = pow(clamp(1.0 - facing, 0.0, 1.0), uExponent);
  float sweep = smoothstep(-0.3, 0.85, vNormalWorld.y * 0.7 + vNormalWorld.x * 0.3);
  vec3 color = mix(uBlue, uCyan, sweep * 0.55);
  float alpha = fresnel * uStrength;
  gl_FragColor = vec4(color, alpha);
}`;

const particleVertex = `
attribute float aSize;
attribute float aTint;
varying float vTint;
void main() {
  vTint = aTint;
  vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
  gl_PointSize = aSize * (6.0 / max(1.0, -mvPosition.z));
  gl_Position = projectionMatrix * mvPosition;
}`;
const particleFragment = `
varying float vTint;
void main() {
  vec2 p = gl_PointCoord - vec2(0.5);
  float d = length(p);
  float core = 1.0 - smoothstep(0.12, 0.5, d);
  float halo = 1.0 - smoothstep(0.22, 0.5, d);
  vec3 c = mix(vec3(0.19, 0.45, 0.88), vec3(0.18, 0.72, 0.87), vTint);
  gl_FragColor = vec4(c, core * 0.42 + halo * 0.025);
}`;

export default function CelestialSphere() {
  const host = useRef(null);

  useEffect(() => {
    const container = host.current;
    if (!container) return undefined;

    let renderer;
    try {
      renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'low-power' });
    } catch {
      container.dataset.webgl = 'unavailable';
      return undefined;
    }

    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.8));
    renderer.setSize(container.clientWidth, container.clientHeight, false);
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.12;
    renderer.setClearColor(0x000000, 0);
    renderer.domElement.setAttribute('aria-hidden', 'true');
    container.appendChild(renderer.domElement);

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(38, container.clientWidth / container.clientHeight, 0.1, 50);
    camera.position.set(0, 0, 4.35);
    const body = new THREE.Group();
    scene.add(body);

    const coreGeometry = new THREE.SphereGeometry(1, 112, 96);
    const coreMaterial = new THREE.ShaderMaterial({
      vertexShader,
      fragmentShader: coreShader,
      uniforms: { uTime: { value: 0 } },
    });
    const core = new THREE.Mesh(coreGeometry, coreMaterial);
    body.add(core);

    const shell = new THREE.Mesh(
      new THREE.SphereGeometry(1.055, 112, 96),
      new THREE.ShaderMaterial({
        vertexShader: atmosphereVertex,
        fragmentShader: atmosphereFragment,
        uniforms: {
          uBlue: { value: new THREE.Color('#1266bb') },
          uCyan: { value: new THREE.Color('#39b8d6') },
          uStrength: { value: 0.36 },
          uExponent: { value: 4.8 },
        },
        transparent: true,
        depthWrite: false,
        blending: THREE.AdditiveBlending,
        side: THREE.BackSide,
      }),
    );
    body.add(shell);

    const haze = new THREE.Mesh(
      new THREE.SphereGeometry(1.18, 80, 72),
      new THREE.ShaderMaterial({
        vertexShader: atmosphereVertex,
        fragmentShader: atmosphereFragment,
        uniforms: {
          uBlue: { value: new THREE.Color('#124982') },
          uCyan: { value: new THREE.Color('#287caa') },
          uStrength: { value: 0.055 },
          uExponent: { value: 1.55 },
        },
        transparent: true,
        depthWrite: false,
        blending: THREE.AdditiveBlending,
        side: THREE.BackSide,
      }),
    );
    body.add(haze);

    const count = 27;
    const positions = new Float32Array(count * 3);
    const sizes = new Float32Array(count);
    const tints = new Float32Array(count);
    for (let i = 0; i < count; i += 1) {
      const theta = Math.acos(2 * Math.random() - 1);
      const phi = Math.random() * Math.PI * 2;
      const radius = 1.23 + Math.random() * 0.28;
      positions[i * 3] = radius * Math.sin(theta) * Math.cos(phi);
      positions[i * 3 + 1] = radius * Math.cos(theta);
      positions[i * 3 + 2] = radius * Math.sin(theta) * Math.sin(phi);
      sizes[i] = 1.0 + Math.random() * 1.7;
      tints[i] = Math.random();
    }
    const particleGeometry = new THREE.BufferGeometry();
    particleGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    particleGeometry.setAttribute('aSize', new THREE.BufferAttribute(sizes, 1));
    particleGeometry.setAttribute('aTint', new THREE.BufferAttribute(tints, 1));
    const particles = new THREE.Points(particleGeometry, new THREE.ShaderMaterial({
      vertexShader: particleVertex,
      fragmentShader: particleFragment,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    }));
    scene.add(particles);

    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let frame = 0;
    let start = performance.now();
    const animate = (now) => {
      frame = requestAnimationFrame(animate);
      const t = (now - start) * 0.001;
      coreMaterial.uniforms.uTime.value = t;
      if (!reducedMotion.matches) {
        body.rotation.y = t * 0.045;
        body.rotation.x = Math.sin(t * 0.14) * 0.018;
        particles.rotation.y = -t * 0.035;
        particles.rotation.x = Math.sin(t * 0.11) * 0.025;
      }
      renderer.render(scene, camera);
    };
    frame = requestAnimationFrame(animate);

    const resize = () => {
      if (!container.clientWidth || !container.clientHeight) return;
      camera.aspect = container.clientWidth / container.clientHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(container.clientWidth, container.clientHeight, false);
    };
    const observer = new ResizeObserver(resize);
    observer.observe(container);

    return () => {
      cancelAnimationFrame(frame);
      observer.disconnect();
      coreGeometry.dispose();
      coreMaterial.dispose();
      shell.geometry.dispose(); shell.material.dispose();
      haze.geometry.dispose(); haze.material.dispose();
      particleGeometry.dispose(); particles.material.dispose();
      renderer.dispose();
      renderer.domElement.remove();
    };
  }, []);

  return (
    <div className="celestial" ref={host} aria-label="Slowly rotating dark blue astronomical sphere">
      <span className="webgl-fallback" aria-hidden="true" />
    </div>
  );
}
