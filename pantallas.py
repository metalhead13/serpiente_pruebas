import pathlib, struct

def fabricante(b):
    w = (b[8] << 8) | b[9]
    return "".join(chr(((w >> s) & 0x1F) + 64) for s in (10, 5, 0))

rutas = list(pathlib.Path("/sys/class/drm").glob("card*-*/edid"))
if not rutas:
    print("No hay salidas de video en /sys/class/drm")

for p in rutas:
    data = p.read_bytes()
    if not data:
        continue
    print(f"=== {p.parent.name} ===")
    print("Fabricante:", fabricante(data))
    print("Codigo de producto:", struct.unpack_from("<H", data, 10)[0])
    serie = struct.unpack_from("<I", data, 12)[0]
    if serie:
        print("Serie numerica:", serie)
    for i in range(4):
        d = data[54 + i * 18:54 + (i + 1) * 18]
        if d[:3] != b"\x00\x00\x00":
            continue
        texto = d[5:18].split(b"\n", 1)[0].decode("ascii", "replace").strip()
        if d[3] == 0xFC:
            print("Modelo:", texto)
        elif d[3] == 0xFF and texto:
            print("Serie:", texto)
