import os
import socket
import sys
import uvicorn


def check_port_available(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind((host, port))
            return True
        except OSError:
            return False


if __name__ == "__main__":
    # 📑 Dynamically reads the PORT assigned by Railway in production.
    # Defaults to 8000 for local fallback development.
    port = int(os.getenv("PORT", 8000))

    if not check_port_available("0.0.0.0", port):
        print(f"[ERROR] Port {port} is already in use. Stop the existing backend process or set PORT to a free port.")
        sys.exit(1)

    print(f"[INFO] Launching production network server on host 0.0.0.0 listening on port: {port}")
    uvicorn.run(
        "backend.app:app",
        host="0.0.0.0",
        port=port,
        reload=False,
    )
