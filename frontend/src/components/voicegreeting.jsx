
import { useEffect, useRef, useState } from "react";

const TTS_API_URL =
  import.meta.env.VITE_TTS_API_URL?.trim() ||
  "/tts";

const GREETING =
  "Hello. I am JOSH, Madhav's personal AI assistant. Welcome. How may I assist you today?";
const VOICE_ENABLED = import.meta.env.VITE_ENABLE_VOICE_GREETING === "true";

export default function VoiceGreeting() {
  const [status, setStatus] = useState("idle");
  const [isPreparing, setIsPreparing] = useState(true);
  const [needsInteraction, setNeedsInteraction] = useState(false);
  const [error, setError] = useState("");

  const audioRef = useRef(null);
  const objectUrlRef = useRef(null);
  const playedRef = useRef(false);

  // Generate greeting when JOSH loads.
  useEffect(() => {
    if (!VOICE_ENABLED) {
      setIsPreparing(false);
      return undefined;
    }
    const controller = new AbortController();
    let cancelled = false;

    async function generateGreeting() {
      try {
        setIsPreparing(true);
        setError("");

        const response = await fetch(TTS_API_URL, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ text: GREETING }),
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`TTS request failed: ${response.status}`);
        }

        const audioBlob = await response.blob();

        if (cancelled) return;

        const audioUrl = URL.createObjectURL(audioBlob);
        objectUrlRef.current = audioUrl;

        const audio = new Audio(audioUrl);
        audioRef.current = audio;

        audio.onended = () => {
          setStatus("idle");
          playedRef.current = true;
        };

        audio.onerror = () => {
          setError("Audio playback failed. Please try again.");
          setStatus("idle");
        };

        // Try automatic playback.
        try {
          await audio.play();

          if (!cancelled) {
            setStatus("speaking");
            setNeedsInteraction(false);
            playedRef.current = true;
          }
        } catch (playError) {
          if (cancelled) return;

          if (playError.name === "NotAllowedError") {
            // Browser blocked autoplay. Wait for user interaction.
            setNeedsInteraction(true);
            setStatus("idle");
          } else {
            throw playError;
          }
        }
      } catch (err) {
        if (cancelled || err.name === "AbortError") return;

        console.error("JOSH voice error:", err);
        setError("Could not generate JOSH's voice. Check the backend.");
        setStatus("idle");
      } finally {
        if (!cancelled) {
          setIsPreparing(false);
        }
      }
    }

    generateGreeting();

    return () => {
      cancelled = true;
      controller.abort();

      audioRef.current?.pause();

      if (objectUrlRef.current) {
        URL.revokeObjectURL(objectUrlRef.current);
        objectUrlRef.current = null;
      }

      audioRef.current = null;
    };
  }, []);

  // Start greeting after the first interaction if autoplay was blocked.
  useEffect(() => {
    if (!needsInteraction) return;

    function activateGreeting() {
      const audio = audioRef.current;

      if (!audio || playedRef.current) return;

      audio.play()
        .then(() => {
          setStatus("speaking");
          setNeedsInteraction(false);
          playedRef.current = true;
        })
        .catch((err) => {
          console.error("JOSH playback error:", err);
        });
    }

    window.addEventListener("pointerdown", activateGreeting);
    window.addEventListener("keydown", activateGreeting);

    return () => {
      window.removeEventListener("pointerdown", activateGreeting);
      window.removeEventListener("keydown", activateGreeting);
    };
  }, [needsInteraction]);

  // Manual voice button.
  async function handleButtonClick() {
    const audio = audioRef.current;

    if (!audio || isPreparing) return;

    if (status === "speaking") {
      audio.pause();
      audio.currentTime = 0;
      setStatus("idle");
      playedRef.current = true;
      return;
    }

    try {
      audio.currentTime = 0;
      await audio.play();

      setStatus("speaking");
      setNeedsInteraction(false);
      playedRef.current = true;
    } catch (err) {
      console.error("JOSH voice error:", err);
      setError("Could not play JOSH's voice.");
    }
  }

  if (!VOICE_ENABLED) return null;

  return (
    <div
      style={{
        position: "fixed",
        bottom: "20px",
        right: "20px",
        zIndex: 9999,
        display: "flex",
        flexDirection: "column",
        alignItems: "flex-end",
        gap: "8px",
      }}
    >
      {needsInteraction && (
        <span style={{ color: "#a8d8ff", fontSize: "12px" }}>
          Tap anywhere to activate JOSH
        </span>
      )}

      {error && (
        <span style={{ color: "#ff9999", fontSize: "12px" }}>
          {error}
        </span>
      )}

      <button
        type="button"
        onClick={handleButtonClick}
        disabled={isPreparing}
        style={{
          padding: "12px 18px",
          borderRadius: "30px",
          border: "1px solid rgba(100,180,255,0.4)",
          background: "rgba(10,20,40,0.92)",
          color: "white",
          cursor: isPreparing ? "wait" : "pointer",
          opacity: isPreparing ? 0.7 : 1,
          backdropFilter: "blur(12px)",
        }}
      >
        {isPreparing && "Preparing JOSH..."}
        {!isPreparing && status === "speaking" && "■ Stop JOSH"}
        {!isPreparing && status === "idle" && "▶ Activate JOSH Voice"}
      </button>
    </div>
  );
}
