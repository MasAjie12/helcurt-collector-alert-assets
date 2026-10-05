# -*- coding: utf-8 -*-
"""Generate HTML Previews for Helcurt Collector Alert & Widgets."""
from pathlib import Path

BASE = Path(__file__).parent
WIDGETS = BASE / "widgets"

# CSS Alert
ALERT_CSS = (BASE / "sociabuzz-alert-obs.css").read_text(encoding="utf-8")

# Template HTML Preview Alert
ALERT_HTML = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Preview Helcurt Collector Alert</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;800;900&family=Rajdhani:wght@700&display=swap" rel="stylesheet">
    <style>
        body {{
            margin: 0;
            padding: 40px 20px;
            background: #0f051d;
            font-family: 'Poppins', sans-serif;
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            box-sizing: border-box;
        }}
        h1 {{
            margin-bottom: 30px;
            color: #f06292;
            text-shadow: 0 0 10px #e91e63;
        }}
        .preview-container {{
            width: 100%;
            max-width: 800px;
            display: flex;
            justify-content: center;
            margin-bottom: 40px;
        }}
        {ALERT_CSS}
    </style>
</head>
<body>
    <h1>Preview Sociabuzz Alert - Helcurt Collector</h1>
    <div class="preview-container">
        <!-- HELCURT COLLECTOR ALERT -->
        <div class="helc-card">
            <img class="helc-bg" src="https://raw.githubusercontent.com/MasAjie12/helcurt-collector-alert-assets/main/bg.jpeg" alt="">
            <div class="helc-veil"></div>
            <div class="helc-spark helc-s1">✦</div>
            <div class="helc-spark helc-s2">✦</div>
            <div class="helc-spark helc-s3">✦</div>
            <div class="helc-spark helc-s4">✦</div>
            <div class="helc-side helc-side-l"></div>
            <div class="helc-side helc-side-r"></div>
            <div class="helc-body">
                <div class="helc-amount">Rp 100.000</div>
                <div class="helc-tag">Saweria / Sociabuzz</div>
                <div class="helc-who">MasAjie12</div>
                <div class="helc-msg">Semangat livestream nya bang Helcurt GG WP!</div>
            </div>
            <div class="helc-shine"></div>
        </div>
    </div>
</body>
</html>
"""

(BASE / "preview-alert.html").write_text(ALERT_HTML, encoding="utf-8")

# Buat Preview Subathon Widget
SUBATHON_CSS = (WIDGETS / "sociabuzz-subathon-obs.css").read_text(encoding="utf-8")
SUBATHON_HTML = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Preview Subathon Helcurt</title>
    <style>
        body {{ background: #0f051d; padding: 40px; display: flex; justify-content: center; }}
        {SUBATHON_CSS}
    </style>
</head>
<body>
    <div id="__next">
        <div style="width: 450px;">
            <div class="chakra-heading">SUBATHON HELCURT</div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 65%;"></div>
            </div>
            <div style="display:flex; justify-content:space-between; margin-top:8px; color:#fff; font-family:sans-serif;">
                <span>Rp 6.500.000</span>
                <span>Target: Rp 10.000.000</span>
            </div>
        </div>
    </div>
</body>
</html>
"""
(BASE / "preview-subathon.html").write_text(SUBATHON_HTML, encoding="utf-8")

print("All preview files built!")
