# projeto-3-snake<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Imagem Neon</title>

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      background: linear-gradient(135deg, #050816, #0f172a, #111827);
      font-family: Arial, sans-serif;
    }

    .container {
      position: relative;
      width: 420px;
      height: 420px;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .orb {
      position: absolute;
      width: 300px;
      height: 300px;
      border-radius: 50%;
      background: radial-gradient(circle at top, #60a5fa, #7c3aed, #0f172a);
      box-shadow:
        0 0 40px #7c3aed,
        0 0 80px #3b82f6,
        0 0 120px #8b5cf6;
      animation: pulse 4s infinite ease-in-out;
    }

    .ring {
      position: absolute;
      width: 360px;
      height: 360px;
      border: 3px solid rgba(255,255,255,0.15);
      border-radius: 50%;
      animation: rotate 12s linear infinite;
    }

    .ring::before {
      content: "";
      position: absolute;
      width: 20px;
      height: 20px;
      background: #38bdf8;
      border-radius: 50%;
      top: -10px;
      left: 50%;
      transform: translateX(-50%);
      box-shadow: 0 0 20px #38bdf8;
    }

    h1 {
      position: absolute;
      color: white;
      font-size: 42px;
      letter-spacing: 4px;
      text-shadow:
        0 0 10px #fff,
        0 0 20px #60a5fa,
        0 0 40px #7c3aed;
      z-index: 10;
    }

    @keyframes rotate {
      from {
        transform: rotate(0deg);
      }
      to {
        transform: rotate(360deg);
      }
    }

    @keyframes pulse {
      0%, 100% {
        transform: scale(1);
      }
      50% {
        transform: scale(1.08);
      }
    }
  </style>
</head>
<body>

  <div class="container">
    <div class="orb"></div>
    <div class="ring"></div>
    <h1>GABRIEL</h1>
  </div>

</body>
</html>
