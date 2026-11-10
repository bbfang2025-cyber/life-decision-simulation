# -*- coding: utf-8 -*-
"""生成《下载与安装》PDF：里面是 Gitee 直连 zip 地址 + 给 AI 的安装指令。"""
import os, subprocess, pathlib

URL = "https://gitee.com/bbfcyber/life-decision-simulation/repository/archive/master.zip"
REPO = "https://gitee.com/bbfcyber/life-decision-simulation"
GH = "https://github.com/bbfang2025-cyber/life-decision-simulation"

OUT = r"D:/Codex探索/open-source/life-decision-simulation/dist"
BUILD = os.path.join(OUT, "build")
os.makedirs(BUILD, exist_ok=True)
HTML_PATH = os.path.join(BUILD, "dl.html")
PDF_PATH = os.path.join(OUT, "人生决策推演_下载与安装.pdf")

HTML = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8"><title>人生决策推演 · 下载与安装</title>
<style>
  @page {{ size: A4; margin: 14mm 14mm 14mm 14mm; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: "Microsoft YaHei","PingFang SC",sans-serif; font-size: 10.4pt; line-height: 1.72;
         color: #161616; margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .kicker {{ font-size: 8.5pt; letter-spacing: .3em; color: #8d8d8d; }}
  h1 {{ font-size: 25pt; margin: 3mm 0 2mm; letter-spacing: -.6pt; }}
  .lead {{ font-size: 11.6pt; color: #333; margin: 0 0 5mm; }}
  .lead b {{ background: linear-gradient(transparent 62%, #ffe98a 62%); }}
  .bar {{ height: 3px; width: 42px; background: #161616; margin-bottom: 6mm; }}

  .urlbox {{ border: 2px solid #161616; padding: 4.5mm 5mm 4mm; margin-bottom: 4mm; }}
  .urlbox .lb {{ font-size: 8.4pt; letter-spacing: .16em; color: #767676; margin-bottom: 2mm; }}
  .urlbox .u {{ font-family: Consolas, monospace; font-size: 9.6pt; line-height: 1.55; word-break: break-all; }}
  .urlbox .tip {{ font-size: 8.6pt; color: #6a6a6a; margin-top: 2.5mm; }}

  .sayit {{ background: #161616; color: #fff; padding: 4.5mm 5mm; margin-bottom: 5mm; }}
  .sayit .lb {{ font-size: 8.2pt; letter-spacing: .18em; opacity: .72; margin-bottom: 2mm; }}
  .sayit p {{ margin: 0; font-size: 10.4pt; line-height: 1.68; }}

  h2 {{ font-size: 11.6pt; margin: 6mm 0 2.4mm; padding-bottom: 1.3mm; border-bottom: 1.4px solid #161616; }}
  h3 {{ font-size: 10.4pt; margin: 4.5mm 0 1.8mm; }}
  p {{ margin: 0 0 2.4mm; }}
  ol, ul {{ margin: 0 0 2.6mm; padding-left: 1.15em; }}
  li {{ margin-bottom: 1.5mm; }}
  .mono {{ font-family: Consolas, monospace; font-size: 9pt; background: #f1f1ec; padding: .3mm 1.2mm; }}
  .box {{ border: 1px solid #d6d6d0; padding: 3.5mm 4mm; margin: 0 0 3mm; font-size: 9.5pt; line-height: 1.66; }}
  .box b {{ color: #000; }}
  .kv {{ font-size: 9.4pt; color: #4a4a4a; }}
  .page2 {{ page-break-before: always; }}
  .step {{ border-left: 3px solid #161616; padding: 1mm 0 1mm 4mm; margin-bottom: 3.2mm; }}
  .step b {{ display: block; margin-bottom: .6mm; }}
  .step span {{ font-size: 9.4pt; color: #3c3c3c; }}
  .foot {{ margin-top: 6mm; border-top: 1px solid #dcdcdc; padding-top: 4mm; font-size: 8.8pt; color: #5e5e5e; }}
</style></head><body>

<div class="kicker">LIFE DECISION SIMULATION</div>
<h1>人生决策推演 · 下载与安装</h1>
<p class="lead">把这份 PDF 丢给你的 AI，它自己能下载、能装好。<br>你也可以照着下面的地址手动下，两分钟搞定。</p>
<div class="bar"></div>

<div class="urlbox">
  <div class="lb">国内直连下载地址（Gitee · 免翻墙 · 已实测可下）</div>
  <div class="u">{URL}</div>
  <div class="tip">电脑上打开会直接开始下载 zip。<b>手机上打开会先进一个「下载仓库」页面，点页面里的下载按钮即可</b>——不是打不开，是它在问你存哪儿。</div>
</div>

<div class="sayit">
  <div class="lb">最省事的用法：把这份 PDF 发给你的 AI，配上这句话</div>
  <p>按这份 PDF 里的地址把这个技能下载并安装到你的技能目录，装完把校验结果和安装路径发我。</p>
</div>

<h2>手动装（三步）</h2>
<div class="step"><b>第一步 · 下载</b><span>复制上面那串地址到浏览器打开，会得到一个 zip。Windows 上如果提示"不常下载"，点"保留"。</span></div>
<div class="step"><b>第二步 · 解压到技能目录</b><span>解压出来通常是一层 <span class="mono">life-decision-simulation-master</span> 文件夹，<b>把里面那层整个文件夹</b>放进去，重命名成 <span class="mono">life-decision-simulation</span>：<br>
  WorkBuddy → <span class="mono">C:\\Users\\你的用户名\\.workbuddy\\skills\\</span><br>
  Claude Code / 桌面版 → <span class="mono">C:\\Users\\你的用户名\\.claude\\skills\\</span></span></div>
<div class="step"><b>第三步 · 确认结构对</b><span>放好之后，路径应该是 <span class="mono">skills\\life-decision-simulation\\SKILL.md</span>——<b>SKILL.md 必须直接在这一层</b>，不要再套一层文件夹，这是最常见的错。</span></div>

<div class="box" style="margin-top:5mm">
  <b>装好之后，测一句就知道有没有生效：</b><br>
  发「我想辞职回老家，收入得减半，你说我该走吗？」<br>
  正常反应是：先用一句话重述你的情况，然后<b>只问一个问题</b>（比如"老家那边工作定了吗"），问完等你答。<br>
  如果它当场甩你一堆建议，说明没装上，回去检查第三点。
</div>

<div class="page2">
  <h2>给 AI 的安装指令（这一页是给机器读的）</h2>
  <p>用户会把这份 PDF 发给你。请按下面执行，不要只做总结。</p>

  <h3>一、下载</h3>
  <p>下载地址：<span class="mono">{URL}</span></p>
  <ul>
    <li>命令行：<span class="mono">curl -L -o lds.zip "{URL}"</span>（Windows PowerShell 用 <span class="mono">Invoke-WebRequest -Uri "{URL}" -OutFile lds.zip</span>）</li>
    <li>下载完先校验：文件应是 zip，大小在 40KB–2MB 之间。拿到的是 HTML 或几十字节的文本，说明被重定向到登录页了，告诉用户改用手动下载。</li>
    <li>如果没有命令行环境，可以用你的浏览器工具打开这个地址下载。</li>
  </ul>

  <h3>二、解压</h3>
  <ul>
    <li>解压后最外层通常是 <span class="mono">life-decision-simulation-master/</span>，里面有 <span class="mono">SKILL.md</span>、<span class="mono">references/</span>、<span class="mono">README.md</span>。</li>
    <li><b>以含 SKILL.md 的那一层为准</b>，把它重命名为 <span class="mono">life-decision-simulation</span>。</li>
  </ul>

  <h3>三、放到技能目录</h3>
  <ul>
    <li>WorkBuddy：<span class="mono">~/.workbuddy/skills/life-decision-simulation/</span></li>
    <li>Claude Code / 桌面版：<span class="mono">~/.claude/skills/life-decision-simulation/</span></li>
    <li>其他工具：找它的 skills / 技能目录，不确定就问用户。目录不存在就先创建。</li>
    <li>最终结构必须是：<span class="mono">skills/life-decision-simulation/SKILL.md</span> + <span class="mono">skills/life-decision-simulation/references/</span>（两个文件）</li>
  </ul>

  <h3>四、校验（必须做完再回话）</h3>
  <ol>
    <li>确认 <span class="mono">SKILL.md</span> 首行是 <span class="mono">---</span>，frontmatter 里 <span class="mono">name: life-decision-simulation</span>。</li>
    <li>确认 <span class="mono">references/提问总库.md</span> 能搜到"第一格"到"第六格"；<span class="mono">references/示范_北京回老家_完整报告.md</span> 能搜到"六问实录"。</li>
    <li>确认 <span class="mono">SKILL.md</span> 里含"六格体检""四位顾问""翻转力"。</li>
    <li>把安装路径和这三项校验结果一起报给用户。</li>
  </ol>

  <h3>五、最后对用户说</h3>
  <div class="box">
    「装好了。现在可以直接说：<b>我在北京做运营五年了，想回老家，收入得减半，女朋友还在异地，我该不该走？</b>」<br>
    「以后想调它，说一句<b>帮我推演一下</b>就行。」
  </div>

  <h3>六、不要做的事</h3>
  <ul>
    <li>不要把 SKILL.md 改名、不要翻译成中文文件名</li>
    <li>不要漏掉 references/（示范案例和 48 问总库是这个技能最值钱的部分）</li>
    <li>不要只写一句"我看过这份文档了"就结束——没有落地文件就等于没装</li>
  </ul>

  <div class="foot">
    项目主页（有说明和更新）：{REPO}　｜　GitHub 镜像：{GH}<br>
    许可证 MIT，可自由修改与商用。示例中的人与数字均为虚构，仅用于演示流程。
  </div>
</div>

</body></html>
"""
open(HTML_PATH, "w", encoding="utf-8").write(HTML)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
       "--virtual-time-budget=5000", f"--print-to-pdf={PDF_PATH}", pathlib.Path(HTML_PATH).as_uri()]
r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
print("rc", r.returncode, r.stderr[-300:])
print("pdf", os.path.exists(PDF_PATH), os.path.getsize(PDF_PATH) if os.path.exists(PDF_PATH) else 0)
