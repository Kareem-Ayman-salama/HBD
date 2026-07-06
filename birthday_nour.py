import base64
from datetime import date
from pathlib import Path

import streamlit as st


BIRTHDAY = date(2000, 7, 6)
HONOREE_NAME = "Dr. Nour"
ARABIC_NAME = "دكتورة نور"
ASSET_DIR = Path(__file__).parent / "assets" / "birthday"


def calculate_age(birthday: date, today: date) -> int:
    """Calculate age in completed years.

    Args:
        birthday: Birth date.
        today: Current date.

    Returns:
        Completed age in years.
    """
    years = today.year - birthday.year
    has_not_had_birthday = (today.month, today.day) < (birthday.month, birthday.day)
    return years - int(has_not_had_birthday)


def svg_data_uri(filename: str) -> str:
    """Convert a local SVG asset into a data URI.

    Args:
        filename: SVG filename inside the birthday assets directory.

    Returns:
        Data URI that can be used in an HTML image tag.
    """
    svg_bytes = (ASSET_DIR / filename).read_bytes()
    encoded_svg = base64.b64encode(svg_bytes).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded_svg}"


def render_styles() -> None:
    """Render page-level CSS styles."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Playfair+Display:wght@700;900&display=swap');

        :root {
            --sage: #AAAE8D;
            --sage-dark: #73775C;
            --burgundy: #45171B;
            --burgundy-soft: #6D252C;
            --cream: #F7F0D8;
            --gold: #D8B56B;
            --ink: #251315;
        }

        html, body, [class*="css"] {
            font-family: "Cairo", sans-serif;
        }

        .stApp {
            background:
                linear-gradient(120deg, rgba(69, 23, 27, 0.07) 0 1px, transparent 1px 24px),
                linear-gradient(135deg, #AAAE8D 0%, #C6C8AA 46%, #F7F0D8 100%);
            color: var(--ink);
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        .birthday-shell {
            max-width: 1120px;
            margin: 0 auto;
            padding: 28px 16px 52px;
            position: relative;
            z-index: 1;
        }

        .hero-card {
            min-height: 84vh;
            display: grid;
            grid-template-columns: 1.02fr 0.98fr;
            overflow: hidden;
            border-radius: 8px;
            background: rgba(247, 240, 216, 0.9);
            border: 1px solid rgba(69, 23, 27, 0.18);
            box-shadow: 0 30px 70px rgba(40, 20, 21, 0.18);
        }

        .visual-panel {
            background:
                radial-gradient(circle at 20% 18%, rgba(247, 240, 216, 0.42), transparent 19%),
                radial-gradient(circle at 74% 76%, rgba(170, 174, 141, 0.22), transparent 30%),
                linear-gradient(145deg, #45171B 0%, #5A1D23 55%, #2E1013 100%);
            color: var(--cream);
            padding: clamp(28px, 5vw, 58px);
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 640px;
        }

        .visual-panel::before {
            content: "";
            position: absolute;
            inset: 22px;
            border: 1px solid rgba(247, 240, 216, 0.34);
            border-radius: 8px;
            pointer-events: none;
        }

        .art-stack {
            position: relative;
            min-height: 420px;
            z-index: 1;
        }

        .hero-art {
            position: absolute;
            width: min(74%, 360px);
            filter: drop-shadow(0 24px 28px rgba(0, 0, 0, 0.24));
            animation: floatSoft 5.4s ease-in-out infinite;
        }

        .hero-art.bouquet {
            top: 2%;
            left: 8%;
            transform: rotate(-8deg);
        }

        .hero-art.gift {
            width: min(44%, 220px);
            right: 6%;
            bottom: 4%;
            animation-delay: .8s;
        }

        .date-seal {
            width: 168px;
            aspect-ratio: 1;
            border-radius: 50%;
            border: 1px solid rgba(247, 240, 216, 0.54);
            display: grid;
            place-items: center;
            text-align: center;
            align-self: flex-end;
            background: rgba(247, 240, 216, 0.09);
            backdrop-filter: blur(6px);
            position: relative;
            z-index: 1;
        }

        .date-seal strong {
            display: block;
            font-family: "Playfair Display", serif;
            font-size: 42px;
            line-height: 1;
        }

        .date-seal span {
            display: block;
            font-size: 15px;
            margin-top: 8px;
        }

        .content-panel {
            padding: clamp(30px, 5vw, 62px);
            display: flex;
            flex-direction: column;
            justify-content: center;
            background:
                radial-gradient(circle at 92% 8%, rgba(69, 23, 27, 0.11), transparent 18%),
                rgba(247, 240, 216, 0.95);
            text-align: right;
            direction: rtl;
        }

        .title-kicker {
            color: var(--burgundy-soft);
            font-size: clamp(17px, 2vw, 21px);
            font-weight: 900;
            margin-bottom: 12px;
        }

        .title {
            font-family: "Playfair Display", serif;
            font-size: clamp(50px, 8vw, 96px);
            line-height: 0.95;
            margin: 0;
            color: var(--burgundy);
            text-align: right;
        }

        .arabic-title {
            font-size: clamp(26px, 4vw, 44px);
            line-height: 1.35;
            margin: 18px 0 8px;
            color: var(--burgundy);
            font-weight: 900;
        }

        .name-line {
            font-size: clamp(22px, 3vw, 34px);
            font-weight: 900;
            color: #30311F;
            margin-bottom: 10px;
        }

        .english-line {
            direction: ltr;
            text-align: right;
            font-family: "Playfair Display", serif;
            font-size: clamp(20px, 2.8vw, 31px);
            color: var(--burgundy-soft);
            margin-bottom: 24px;
        }

        .wish {
            font-size: clamp(17px, 2.1vw, 22px);
            line-height: 1.95;
            color: #372125;
            margin: 0 0 30px;
        }

        .mini-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 10px;
            margin-bottom: 26px;
        }

        .mini-card {
            min-height: 132px;
            border-radius: 8px;
            background: rgba(170, 174, 141, 0.32);
            border: 1px solid rgba(69, 23, 27, 0.16);
            display: grid;
            place-items: center;
            text-align: center;
            padding: 12px 8px;
        }

        .mini-card img {
            width: 76px;
            height: 76px;
            object-fit: contain;
            display: block;
            margin: 0 auto;
        }

        .mini-card span {
            display: block;
            margin-top: 8px;
            font-size: 14px;
            font-weight: 900;
            color: var(--burgundy);
        }

        .footer-strip {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            border-top: 1px solid rgba(69, 23, 27, 0.18);
            padding-top: 20px;
        }

        .age-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 50px;
            padding: 0 20px;
            border-radius: 999px;
            background: var(--burgundy);
            color: var(--cream);
            font-size: 18px;
            font-weight: 900;
        }

        .birthday-note {
            direction: ltr;
            color: #4F503A;
            font-size: 14px;
            font-weight: 800;
        }

        .message-band {
            margin-top: 18px;
            padding: 26px 24px;
            border-radius: 8px;
            background: rgba(69, 23, 27, 0.93);
            color: var(--cream);
            text-align: center;
            font-size: clamp(18px, 2.2vw, 24px);
            line-height: 1.9;
            direction: rtl;
        }

        .message-band em {
            display: block;
            direction: ltr;
            font-family: "Playfair Display", serif;
            font-size: clamp(18px, 2.4vw, 26px);
            color: #DCD8B6;
            margin-top: 12px;
            font-style: normal;
        }

        .petal {
            position: fixed;
            top: -10vh;
            left: var(--x);
            width: var(--size);
            height: calc(var(--size) * 1.38);
            border-radius: 64% 36% 62% 38%;
            background: var(--color);
            animation: fall var(--duration) linear infinite;
            animation-delay: var(--delay);
            opacity: 0.45;
            pointer-events: none;
            z-index: 0;
        }

        @keyframes floatSoft {
            0%, 100% { translate: 0 0; }
            50% { translate: 0 -12px; }
        }

        @keyframes fall {
            0% { transform: translateY(-12vh) rotate(0deg); }
            100% { transform: translateY(112vh) rotate(240deg); }
        }

        @media (max-width: 860px) {
            .hero-card {
                grid-template-columns: 1fr;
            }

            .visual-panel {
                min-height: 450px;
            }

            .art-stack {
                min-height: 300px;
            }

            .mini-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_petals() -> None:
    """Render subtle animated petals using CSS shapes."""
    petals = [
        ("7%", "14px", "10s", "0s", "#6D252C"),
        ("16%", "10px", "12s", "1s", "#F7F0D8"),
        ("27%", "13px", "14s", "3s", "#45171B"),
        ("41%", "11px", "11s", "2s", "#D8B56B"),
        ("55%", "15px", "13s", "4s", "#73775C"),
        ("70%", "10px", "10s", "1.5s", "#6D252C"),
        ("83%", "13px", "15s", "0.5s", "#F7F0D8"),
        ("94%", "12px", "12s", "2.5s", "#45171B"),
    ]
    html = "\n".join(
        (
            f'<span class="petal" style="--x:{x}; --size:{size}; '
            f'--duration:{duration}; --delay:{delay}; --color:{color};"></span>'
        )
        for x, size, duration, delay, color in petals
    )
    st.markdown(html, unsafe_allow_html=True)


def render_page() -> None:
    """Render the birthday Streamlit page."""
    today = date.today()
    age = calculate_age(BIRTHDAY, today)
    birthday_label = BIRTHDAY.strftime("%d / %m / %Y")
    bouquet_uri = svg_data_uri("bouquet.svg")
    gift_uri = svg_data_uri("gift.svg")
    candles_uri = svg_data_uri("candles.svg")
    note_uri = svg_data_uri("love_note.svg")

    render_styles()
    render_petals()

    st.markdown(
        f"""
        <main class="birthday-shell">
            <section class="hero-card">
                <aside class="visual-panel">
                    <div class="art-stack">
                        <img class="hero-art bouquet" src="{bouquet_uri}" alt="Rose bouquet">
                        <img class="hero-art gift" src="{gift_uri}" alt="Wrapped gift">
                    </div>
                    <div class="date-seal">
                        <div>
                            <strong>06</strong>
                            <span>July 2000</span>
                        </div>
                    </div>
                </aside>
                <section class="content-panel">
                    <div class="title-kicker">A little birthday page made with love</div>
                    <h1 class="title">Happy<br>Birthday</h1>
                    <div class="arabic-title">عيد ميلاد سعيد</div>
                    <div class="name-line">{ARABIC_NAME}</div>
                    <div class="english-line">To the brilliant {HONOREE_NAME}</div>
                    <p class="wish">
                        كل سنة وأنتِ طيبة يا نور. ربنا يجعل سنتك الجديدة هادية،
                        ناجحة، ومليانة لحظات دافية تليق بقلبك. يومك مش مجرد تاريخ،
                        ده فرصة نقول لك إن وجودك نور حقيقي، وإنك تستاهلي كل وردة
                        وكل شمعة وكل دعوة حلوة.
                    </p>
                    <div class="mini-grid">
                        <div class="mini-card">
                            <div>
                                <img src="{bouquet_uri}" alt="Roses drawing">
                                <span>Roses</span>
                            </div>
                        </div>
                        <div class="mini-card">
                            <div>
                                <img src="{candles_uri}" alt="Candles drawing">
                                <span>Wishes</span>
                            </div>
                        </div>
                        <div class="mini-card">
                            <div>
                                <img src="{note_uri}" alt="Love note drawing">
                                <span>Love</span>
                            </div>
                        </div>
                        <div class="mini-card">
                            <div>
                                <img src="{gift_uri}" alt="Gift drawing">
                                <span>Gifts</span>
                            </div>
                        </div>
                    </div>
                    <div class="footer-strip">
                        <div class="age-badge">أتمت {age} سنة</div>
                        <div class="birthday-note">Born on {birthday_label}</div>
                    </div>
                </section>
            </section>
            <section class="message-band">
                يا رب السنة الجاية تبقى أحن، أوسع، وأنجح.
                وتفضلي دايما قريبة من أحلامك ومن كل حاجة بتحبيها.
                <em>May your new year be soft, bright, and full of beautiful wins.</em>
            </section>
        </main>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    """Configure and render the Streamlit app."""
    st.set_page_config(
        page_title="Birthday for Dr. Nour",
        page_icon="🎂",
        layout="wide",
    )
    render_page()


if __name__ == "__main__":
    main()
