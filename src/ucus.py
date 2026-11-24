cat << 'EOF' > ucus.py
import asyncio
from mavsdk import System


async def telemetri_izle(drone: System):
    konum = None
    hiz_ms = 0.0
    havada_mi = False
    ucus_modu = "UNKNOWN"

    async def konum_takip():
        nonlocal konum
        async for pos in drone.telemetry.position():
            konum = pos

    async def hiz_takip():
        nonlocal hiz_ms
        async for vel in drone.telemetry.velocity_ned():
            hiz_ms = (vel.north_m_s ** 2 + vel.east_m_s ** 2) ** 0.5

    async def havada_takip():
        nonlocal havada_mi
        async for in_air in drone.telemetry.in_air():
            havada_mi = in_air

    async def mod_takip():
        nonlocal ucus_modu
        async for mode in drone.telemetry.flight_mode():
            ucus_modu = str(mode)

    gorevler = [
        asyncio.create_task(konum_takip()),
        asyncio.create_task(hiz_takip()),
        asyncio.create_task(havada_takip()),
        asyncio.create_task(mod_takip()),
    ]

    try:
        while True:
            if konum is not None:
                print(
                    f"Konum: ({konum.latitude_deg:.6f}, {konum.longitude_deg:.6f}) | "
                    f"Irtifa: {konum.relative_altitude_m:.1f} m | "
                    f"Hiz: {hiz_ms:.1f} m/s | "
                    f"Havada: {havada_mi} | "
                    f"Mod: {ucus_modu}"
                )
            await asyncio.sleep(2)
    finally:
        for g in gorevler:
            g.cancel()


async def run():
    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    print("1) IHA baglantisi bekleniyor...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("   Baglandi!")
            break

    telemetri_gorevi = asyncio.create_task(telemetri_izle(drone))

    print("2) IHA arm ediliyor...")
    await drone.action.arm()

    print("3) Mission baslatiliyor...")
    await drone.mission.start_mission()

    async for progress in drone.mission.mission_progress():
        print(f"   Mission ilerlemesi: {progress.current}/{progress.total}")
        if progress.current == progress.total and progress.total > 0:
            break

    print("4) Gorev adimlari tamamlandi, inis sureci izleniyor...")
    await asyncio.sleep(20)
    telemetri_gorevi.cancel()


if __name__ == "__main__":
    asyncio.run(run())
EOF
