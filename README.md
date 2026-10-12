# ⏱️ Chronos Luxe Clock & Built-in Device Emulator

A clock web application built with Vanilla HTML5, CSS3, and JavaScript, featuring an interactive hardware emulator shell, multi-feature chronometer, world clock, customizable alarms, timer, and synthesized ambient sleep soundscape.

---

## 🌟 Key Features

1. **Integrated Device Emulator Chassis**
   - **iPhone 16 Pro Frame**: Dynamic Island with live status, status bar (5G, WiFi, battery indicator), and home indicator bar.
   - **Google Pixel Mode**: Android chassis with camera punch-hole and edge rounding.
   - **Smartwatch / Wearable Mode**: Compact smartwatch display.
   - **Fullscreen / Desktop Mode**: Full adaptive viewport.
   - **Rotate Screen**: Landscape and portrait toggle.
   - **Theme Switcher**: 4 themes (*Midnight Titanium*, *Cyberpunk Neon*, *Obsidian Gold*, and *Frost Glass*).

2. **Luxury Analog & Digital Clock**
   - Continuous 60 FPS sweeping second hand with realistic mechanical clock physics.
   - 12 hour dial markers with complication date window (`OCT 13`).
   - Digital OLED card showing local time, AM/PM, seconds, day/date, and timezone badge.
   - Instant toggle between **Analog Luxe** and **Digital OLED** views.

3. **World Clock**
   - Multi-timezone tracking (New York, London, Tokyo, Dubai, Sydney, and more).
   - Real-time time calculations and day/hour relative offset indicators.
   - "+ Add World Clock" modal with capital cities directory.

4. **Alarms with Synthesizer Tones**
   - Set custom alarms with time picker, custom label, and tone selectors.
   - Countdown banner indicating time remaining until the next scheduled alarm.
   - Ringing alarm overlay with interactive **Snooze (+5 min)** and **Dismiss** actions.
   - Synthesized ringtones: *Digital Radar Chime*, *Zen Bell Resonance*, and *Cyber Electronic Pulse*.

5. **Stopwatch (Precision Chronometer)**
   - Sub-millisecond tracking (`MM:SS.ms`) powered by `performance.now()`.
   - Circular SVG second rotation track.
   - Start, pause, resume, reset, and lap recording.
   - Lap history table highlighting the **Fastest / Best Lap** (green) and **Slowest Lap** (red).

6. **Radial Timer & Presets**
   - Animated radial circular progress countdown ring.
   - Quick presets: `1 min`, `5 min`, `10 min`, `15 min`, `25m Focus (Pomodoro)`, `45m Deep Work`.
   - Custom Hours, Minutes, and Seconds inputs.
   - `+1 Min` extension button on the fly.
   - Completion chime and alert.

7. **Sleep & Ambient Sound Machine**
   - **90-Minute Sleep Cycle Calculator**: Computes optimal wake-up times (3, 4, 5, or 6 cycles) based on current bedtime. Click any cycle to automatically set an alarm!
   - **Web Audio Sleep Synthesizer**: Generates *Soft Rain*, *Brown Noise*, *White Noise*, and *Zen Resonance* directly in the browser with an audio visualizer.

---

## 🚀 How to Open in Built-in Emulator / Browser

The local server is already running on **`http://localhost:3000`**.

### In Antigravity IDE / VS Code:
1. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac).
2. Type and select **`Simple Browser: Show`**.
3. Enter:
   ```text
   http://localhost:3000
   ```
4. The Clock app will open right inside the IDE tab / split panel next to your code!

### In External Browser:
- Simply open [http://localhost:3000](http://localhost:3000) in Chrome, Edge, Brave, or Firefox.

### Running Manually:
```powershell
python server.py
```
