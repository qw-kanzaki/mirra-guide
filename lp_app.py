from __future__ import annotations

import html

import streamlit as st

LINE_ADD_FRIEND_URL = "https://lin.ee/Rj8mglD"


st.set_page_config(
    page_title="MIRRA｜今の自分を見るためのタロット",
    page_icon="🪞",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      :root {
        color-scheme: light;
        --ink: #17243a;
        --ink-soft: #465065;
        --navy: #0d1a30;
        --navy-light: #182945;
        --paper: #f8f6f0;
        --paper-deep: #f0ece2;
        --white: #fffdfa;
        --gold: #aa8b49;
        --gold-light: #d7c18e;
        --line: #d8d2c5;
      }

      html { scroll-behavior: smooth; }
      body {
        margin: 0;
        background: var(--paper);
        color: var(--ink);
        font-family: "Noto Sans JP", "Hiragino Sans", "Yu Gothic UI", "Yu Gothic", sans-serif;
        -webkit-font-smoothing: antialiased;
      }
      .stApp { background: var(--paper); }
      .block-container {
        width: 100%;
        max-width: none;
        padding: 0 !important;
      }
      [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], #MainMenu, footer { display: none !important; }
      [data-testid="stAppViewContainer"] > .main { padding-top: 0 !important; }
      div[data-testid="stMarkdownContainer"] > p { margin: 0; }

      .mirra-lp, .mirra-lp * { box-sizing: border-box; }
      .mirra-lp {
        overflow: hidden;
        background: var(--paper);
        color: var(--ink);
        font-size: 1rem;
        line-height: 2;
      }
      .lp-shell {
        width: min(100% - 40px, 680px);
        margin-inline: auto;
      }
      .lp-brand {
        margin: 0;
        color: var(--gold-light);
        font-family: Georgia, "Times New Roman", serif;
        font-size: .82rem;
        font-weight: 600;
        letter-spacing: .42em;
        line-height: 1;
      }
      .lp-hero {
        min-height: min(100svh, 820px);
        display: grid;
        align-items: center;
        padding: calc(48px + env(safe-area-inset-top, 0px)) 0 64px;
        background:
          radial-gradient(circle at 84% 16%, rgba(215,193,142,.13), transparent 30%),
          linear-gradient(152deg, #0b172a 0%, #14243d 56%, #0c192e 100%);
        color: #f8f4ea;
        border-bottom: 1px solid rgba(170,139,73,.65);
      }
      .lp-hero__inner { width: min(100% - 40px, 720px); margin-inline: auto; }
      .lp-hero__rule {
        width: 42px;
        height: 1px;
        margin: 30px 0 34px;
        background: var(--gold);
      }
      .lp-hero h1 {
        max-width: 650px;
        margin: 0;
        color: #fffdf8;
        font-family: "Noto Serif JP", "Yu Mincho", "Hiragino Mincho ProN", serif;
        font-size: clamp(2rem, 8.4vw, 4.3rem);
        font-weight: 600;
        letter-spacing: .015em;
        line-height: 1.5;
      }
      .lp-hero__opening {
        margin: 44px 0 0;
        color: #f8f4ea;
        font-size: clamp(1.06rem, 4.4vw, 1.25rem);
        font-weight: 600;
        line-height: 1.9;
      }
      .lp-hero__body {
        max-width: 600px;
        margin: 24px 0 0;
        color: #e5e0d5;
        font-size: 1rem;
        line-height: 2.05;
      }
      .lp-hero__body strong { color: #f2dca4; }

      .lp-section { padding: 96px 0; }
      .lp-section--paper-deep {
        background: var(--paper-deep);
        border-block: 1px solid var(--line);
      }
      .lp-section--navy {
        background: var(--navy);
        color: #f3efe6;
        border-block: 1px solid rgba(170,139,73,.55);
      }
      .lp-section h2 {
        margin: 0 0 48px;
        color: var(--ink);
        font-family: "Noto Serif JP", "Yu Mincho", "Hiragino Mincho ProN", serif;
        font-size: clamp(1.62rem, 6.7vw, 2.45rem);
        font-weight: 600;
        letter-spacing: .01em;
        line-height: 1.55;
        line-break: strict;
        text-wrap: balance;
      }
      .lp-section--navy h2 { color: #fffdf8; }
      .lp-section p { margin: 0 0 26px; color: var(--ink-soft); }
      .lp-section--navy p { color: #ded9cf; }
      .lp-section strong { color: var(--ink); font-weight: 750; }
      .lp-section--navy strong { color: #f1d796; }
      .lp-section p:last-child { margin-bottom: 0; }
      .lp-section__rule {
        width: 40px;
        height: 1px;
        margin: 0 0 48px;
        background: var(--gold);
      }
      .lp-lines { display: grid; gap: 30px; }
      .lp-lines p { margin: 0; }
      .lp-question-list {
        display: grid;
        gap: 0;
        margin: 0 0 54px;
        border-top: 1px solid var(--line);
      }
      .lp-question {
        margin: 0 !important;
        padding: 25px 0;
        border-bottom: 1px solid var(--line);
      }
      .lp-emphasis {
        margin: 48px 0 !important;
        padding: 26px 0 26px 25px;
        border-left: 2px solid var(--gold);
        color: var(--ink) !important;
        font-family: "Noto Serif JP", "Yu Mincho", "Hiragino Mincho ProN", serif;
        font-size: 1.12rem;
      }
      .lp-section--navy .lp-emphasis { color: #fffdf8 !important; }
      .lp-quote {
        margin: 34px 0 !important;
        padding: 22px 24px;
        background: rgba(255,255,255,.58);
        border: 1px solid var(--line);
        color: var(--ink) !important;
        font-family: "Noto Serif JP", "Yu Mincho", "Hiragino Mincho ProN", serif;
        font-size: 1.05rem;
        text-align: center;
      }
      .jp-keep { white-space: nowrap; }

      .lp-cta-section {
        padding: 80px 0;
        background:
          radial-gradient(circle at 50% 0, rgba(215,193,142,.13), transparent 32%),
          var(--navy);
        color: #f8f4ea;
        text-align: center;
      }
      .lp-cta-section h2 {
        margin: 0 0 22px;
        color: #fffdf8;
        font-family: "Noto Serif JP", "Yu Mincho", "Hiragino Mincho ProN", serif;
        font-size: clamp(1.75rem, 7vw, 2.6rem);
        font-weight: 600;
        line-height: 1.55;
      }
      .lp-cta-section p { margin: 0 0 22px; color: #ded9cf; }
      .lp-cta-section strong { color: #f2dca4; }
      .lp-mini-map {
        display: inline-block;
        margin: 10px auto 42px;
        padding: 14px 24px;
        border-block: 1px solid rgba(215,193,142,.55);
        color: #f2dca4;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 1.05rem;
        font-weight: 600;
        letter-spacing: .08em;
      }
      .lp-cta {
        display: flex;
        align-items: center;
        justify-content: center;
        width: min(100%, 520px);
        min-height: 62px;
        margin: 42px auto 20px;
        padding: 16px 22px;
        border: 1px solid #d8bf7d;
        border-radius: 8px;
        background: linear-gradient(180deg, #c9ab65, #a9873f);
        box-shadow: 0 14px 34px rgba(0,0,0,.24);
        color: #0b172a !important;
        font-size: 1rem;
        font-weight: 800;
        letter-spacing: .02em;
        line-height: 1.55;
        text-decoration: none !important;
        transition: transform .18s ease, box-shadow .18s ease, background .18s ease;
      }
      .lp-cta:hover {
        transform: translateY(-2px);
        background: linear-gradient(180deg, #dbc184, #b6964f);
        box-shadow: 0 17px 40px rgba(0,0,0,.3);
      }
      .lp-cta:focus-visible { outline: 3px solid #fff4ca; outline-offset: 4px; }
      .lp-cta-note { margin: 0 !important; color: #cfc9bd !important; font-size: .92rem; }
      .lp-cta-assurance { margin-top: 8px !important; color: #f2dca4 !important; }

      .lp-story { position: relative; }
      .lp-story::before {
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        left: -42px;
        width: 1px;
        background: linear-gradient(transparent, var(--gold), transparent);
      }
      .lp-finale { padding-bottom: calc(96px + env(safe-area-inset-bottom, 0px)); }

      @media (max-width: 540px) {
        .lp-shell, .lp-hero__inner { width: min(100% - 40px, 680px); }
        .lp-hero { min-height: 100svh; padding-bottom: 52px; }
        .lp-hero__rule { margin-block: 25px 30px; }
        .lp-hero h1 {
          max-width: 100%;
          font-size: 1.65rem;
          letter-spacing: 0;
          line-height: 1.55;
          line-break: strict;
          text-wrap: wrap;
        }
        .lp-hero h1 .hero-break { display: none; }
        .lp-hero__opening { margin-top: 38px; }
        .lp-hero__body { margin-top: 20px; line-height: 1.95; }
        .lp-section { padding: 76px 0; }
        .lp-section h2 {
          margin-bottom: 38px;
          font-size: 1.5rem;
          letter-spacing: 0;
          line-height: 1.55;
        }
        .lp-section p { margin-bottom: 22px; line-height: 1.95; }
        .lp-question { padding-block: 22px; }
        .lp-emphasis { margin-block: 40px !important; padding: 21px 0 21px 19px; }
        .lp-quote { margin-block: 28px !important; padding: 18px 16px; }
        .lp-cta-section { padding: 72px 0; }
        .lp-cta { min-height: 60px; margin-top: 36px; padding-inline: 17px; }
        .lp-story::before { display: none; }
      }

      @media (min-width: 900px) {
        .lp-hero__inner { width: min(100% - 96px, 1120px); }
        .lp-hero h1 { max-width: none; font-size: clamp(3.4rem, 5vw, 4.3rem); }
        .lp-hero__body { max-width: 660px; }
        .lp-section { padding-block: 120px; }
        .lp-shell { width: min(100% - 96px, 720px); }
      }

      @media (prefers-reduced-motion: reduce) {
        html { scroll-behavior: auto; }
        .lp-cta { transition: none; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

safe_line_url = html.escape(LINE_ADD_FRIEND_URL, quote=True)

st.markdown(
    f"""
    <main class="mirra-lp">
      <section class="lp-hero">
        <div class="lp-hero__inner">
          <p class="lp-brand">MIRRA</p>
          <div class="lp-hero__rule"></div>
          <h1>未来を当てるためじゃなく、<br class="hero-break">今の自分を見るためのタロット。</h1>
          <p class="lp-hero__opening">「どうしたらいいんだろう」</p>
          <div class="lp-hero__body">
            <p>答えは欲しい。<br>でも、誰かに人生を決めてほしいわけじゃない。</p>
            <p>MIRRAは、カードを「答え」ではなく、</p>
            <p><strong>自分では見えにくくなっている自分を見るための鏡</strong></p>
            <p>として使うタロットです。</p>
          </div>
        </div>
      </section>

      <section class="lp-section">
        <div class="lp-shell">
          <h2>こんなこと、ありませんか？</h2>
          <div class="lp-question-list">
            <p class="lp-question">相手のことを考えているうちに、<br><strong>自分がどうしたいのか分からなくなる。</strong></p>
            <p class="lp-question">頭では分かっているのに、<br><strong>なぜか同じところで迷ってしまう。</strong></p>
            <p class="lp-question">何度考えても、<br><strong>どの答えもしっくりこない。</strong></p>
            <p class="lp-question">「こうした方がいい」と思うのに、<br><strong>気持ちがついてこない。</strong></p>
          </div>
          <p>そんな時、</p>
          <p>もっと答えを探す前に、</p>
          <p class="lp-emphasis"><strong>自分が今、何を怖がって、何を守ろうとしているのか。</strong></p>
          <p>そこを一度見てみると、<br>今までとは違う見え方が出てくることがあります。</p>
        </div>
      </section>

      <section class="lp-section lp-section--paper-deep">
        <div class="lp-shell">
          <h2>MIRRAが見るのは、<span class="jp-keep">未来ではありません。</span></h2>
          <div class="lp-lines">
            <p>たとえば、</p>
            <p class="lp-quote">「返信が来なくて不安」</p>
            <p>という悩みでも、</p>
            <p>ただ返信が欲しいだけではなく、</p>
            <p><strong>「この関係は大丈夫」と確認したい</strong></p>
            <p>気持ちが混ざっていることもあります。</p>
            <p>転職で迷っている時も、</p>
            <p>「辞めたい・辞めたくない」だけではなく、</p>
            <p><strong>周りからどう見られるか</strong></p>
            <p>が判断を重くしていることもあります。</p>
            <p>MIRRAでは、</p>
            <p>カードとあなた自身の言葉を手がかりに、</p>
            <p><strong>自分ではまだ整理できていない気持ちや、</strong><br><strong>考え方のつながり</strong></p>
            <p>を見ていきます。</p>
          </div>
        </div>
      </section>

      <section class="lp-cta-section">
        <div class="lp-shell">
          <h2>まずは、自分の場合を見てみる。</h2>
          <p>無料1枚鑑定では、</p>
          <p>今悩んでいることを書いて、<br><strong>自分でカードを1枚引きます。</strong></p>
          <p>その1枚をきっかけに、</p>
          <p><strong>「今、自分の中で何が起きているのか」</strong></p>
          <p>を整理します。</p>
          <p>鑑定の最後には、<br>今の状態を簡単に整理した</p>
          <div class="lp-mini-map">Mini Inner Map</div>
          <p>もお届けします。</p>
          <a class="lp-cta" href="{safe_line_url}">無料1枚鑑定を受けてみる</a>
          <p class="lp-cta-note">LINE友だち追加後、そのまま無料鑑定へ進めます。</p>
          <p class="lp-cta-assurance"><strong>無料鑑定だけで終えても大丈夫です。</strong></p>
        </div>
      </section>

      <section class="lp-section lp-story">
        <div class="lp-shell">
          <h2>私も、<span class="jp-keep">自分で選んでいる</span><span class="jp-keep">つもりでした。</span></h2>
          <p>仕事でも、人間関係でも、恋愛でも。</p>
          <p>その時の自分なりに考えて、<br>ちゃんと選んできたつもりでした。</p>
          <p>でも、うまくいかないことを何度か経験する中で、</p>
          <p>ひとつ気づいたことがありました。</p>
          <p class="lp-emphasis"><strong>選択肢を選ぶ前に、</strong><br><strong>「何が正しいと思うか」そのものに、</strong><br><strong>自分の“当たり前”が入り込んでいる。</strong></p>
          <p>自分では自由に選んでいるつもりでも、</p>
          <p>何を選択肢に入れるか。<br>何を怖いと思うか。<br>何なら自分にできると思うか。</p>
          <p>その基準までは、<br>自分ではなかなか見えません。</p>
          <p>そこに気づいてから、</p>
          <p>同じ出来事でも、<br>少しずつ違う選び方ができるようになりました。</p>
          <p><strong>今まで見えていなかった選択肢が、</strong><br><strong>少しずつ見えるようになった。</strong></p>
          <p>その積み重ねで、<br>人生の進み方も変わってきたと感じています。</p>
          <p>MIRRAで大切にしているのも、</p>
          <p><strong>答えをもらうことではなく、</strong><br><strong>自分では見えていなかった自分に気づくこと。</strong></p>
          <p>です。</p>
        </div>
      </section>

      <section class="lp-section lp-section--navy">
        <div class="lp-shell">
          <h2>「こうするべき」ではなく、<br>もう一つの見方を増やす。</h2>
          <div class="lp-section__rule"></div>
          <p>MIRRAは、</p>
          <p>相手の気持ちを事実のように断定しません。</p>
          <p>未来を決めつけません。</p>
          <p>不安を煽りません。</p>
          <p>そして、</p>
          <p class="lp-emphasis"><strong>「あなたはこうするべき」</strong></p>
          <p>と人生の答えを決めることもしません。</p>
          <p>今まで、</p>
          <p>「AかBしかない」</p>
          <p>と思っていたところに、</p>
          <p><strong>「こんな見方もあったのか」</strong></p>
          <p>がひとつ増える。</p>
          <p>その結果、</p>
          <p>自分で選びやすくなる。</p>
          <p>MIRRAが目指しているのは、<br>そんな鑑定です。</p>
        </div>
      </section>

      <section class="lp-section lp-section--paper-deep">
        <div class="lp-shell">
          <h2>カードは、答えではなく鏡。</h2>
          <p>カードそのものが、</p>
          <p>「あなたはこういう人です」</p>
          <p>と決めるわけではありません。</p>
          <p>カードをきっかけに、</p>
          <p>何が引っかかるのか。</p>
          <p>何に違和感を持つのか。</p>
          <p>どんな言葉なら、<br>今の自分にしっくりくるのか。</p>
          <p>そこにも、<br>自分を見るヒントがあります。</p>
          <p>だからMIRRAでは、</p>
          <p><strong>当たった・外れた</strong></p>
          <p>だけで終わらせません。</p>
          <p>カードをきっかけに、</p>
          <p class="lp-emphasis"><strong>自分では気づきにくかった自分を、</strong><br><strong>少し離れたところから見てみる。</strong></p>
          <p>そのためにタロットを使います。</p>
        </div>
      </section>

      <section class="lp-cta-section lp-finale">
        <div class="lp-shell">
          <h2>今の自分を、1枚だけ映してみる。</h2>
          <p>大きな悩みでなくても大丈夫です。</p>
          <p>恋愛でも、仕事でも、人間関係でも。</p>
          <p>「なんとなく引っかかっている」</p>
          <p>くらいでも構いません。</p>
          <p>まずは1枚、</p>
          <p><strong>今の自分を見るために引いてみてください。</strong></p>
          <a class="lp-cta" href="{safe_line_url}">自分の場合を無料1枚鑑定で見てみる</a>
          <p class="lp-cta-note">LINE友だち追加後、そのまま無料鑑定へ進めます。</p>
          <p class="lp-cta-note">料金はかかりません。</p>
          <p class="lp-cta-assurance"><strong>無料鑑定だけで終了しても大丈夫です。</strong></p>
        </div>
      </section>
    </main>
    """,
    unsafe_allow_html=True,
)
