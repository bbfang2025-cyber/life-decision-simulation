# -*- coding: utf-8 -*-
"""生成《下载与安装》PDF v2：
用户只需要说一句「帮我下载安装并调用这个 skill」，
其余所有分支（下载失败、解压、装哪、调不出来、工具不支持技能…）全部写在给 AI 的手册里。
"""
import os, subprocess, pathlib

URL = "https://gitee.com/bbfcyber/life-decision-simulation/releases/download/v1.0.0/life-decision-simulation_v1.0.0.zip"
URL_TAG = "https://gitee.com/bbfcyber/life-decision-simulation/repository/archive/v1.0.0.zip"
URL_MASTER = "https://gitee.com/bbfcyber/life-decision-simulation/repository/archive/master.zip"
URL_GH = "https://github.com/bbfang2025-cyber/life-decision-simulation/releases/download/v1.0.0/life-decision-simulation_v1.0.0.zip"
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
  @page {{ size: A4; margin: 13mm 14mm 13mm 14mm; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: "Microsoft YaHei","PingFang SC",sans-serif; font-size: 9.7pt; line-height: 1.55;
         color: #161616; margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .kicker {{ font-size: 8.5pt; letter-spacing: .3em; color: #8d8d8d; }}
  h1 {{ font-size: 20pt; margin: 2mm 0 1.4mm; letter-spacing: -.6pt; }}
  .lead {{ font-size: 10.4pt; color: #333; margin: 0 0 2.8mm; }}
  .bar {{ height: 3px; width: 42px; background: #161616; margin-bottom: 3.4mm; }}

  .tag {{ background: #161616; color: #fff; font-size: 8.1pt; letter-spacing: .04em;
          padding: 1.6mm 3mm; margin-bottom: 3mm; line-height: 1.5; }}

  .urlbox {{ border: 2px solid #161616; padding: 2.8mm 4mm 2.4mm; margin-bottom: 2.8mm; }}
  .urlbox .lb {{ font-size: 8.2pt; letter-spacing: .14em; color: #767676; margin-bottom: 1.6mm; }}
  .urlbox .u {{ font-family: Consolas, monospace; font-size: 8.9pt; line-height: 1.5; word-break: break-all; }}
  .urlbox .tip {{ font-size: 8.2pt; color: #6a6a6a; margin-top: 1.8mm; }}
  .urlbox .alt {{ margin-top: 1.6mm; }}
  .urlbox .alt div {{ margin-bottom: 1.1mm; }}

  .sayit {{ background: #161616; color: #fff; padding: 3.2mm 4.4mm 3mm; margin-bottom: 3mm; }}
  .sayit .lb {{ font-size: 8pt; letter-spacing: .18em; opacity: .75; margin-bottom: 1.6mm; }}
  .sayit .big {{ font-size: 14pt; font-weight: 700; letter-spacing: .02em; margin: 0 0 1.4mm; }}
  .sayit p {{ margin: 0; font-size: 8.7pt; line-height: 1.52; opacity: .9; }}

  h2 {{ font-size: 10.4pt; margin: 3.4mm 0 1.6mm; padding-bottom: .9mm; border-bottom: 1.4px solid #161616; }}
  h3 {{ font-size: 9.8pt; margin: 3.4mm 0 1.3mm; }}
  p {{ margin: 0 0 1.8mm; }}
  ol, ul {{ margin: 0 0 2mm; padding-left: 1.15em; }}
  li {{ margin-bottom: 1mm; }}
  .mono {{ font-family: Consolas, monospace; font-size: 8.4pt; background: #f1f1ec; padding: .2mm 1.2mm; }}
  .box {{ border: 1px solid #d6d6d0; padding: 2.4mm 3.2mm; margin: 0 0 2mm; font-size: 8.8pt; line-height: 1.52; }}
  .box.dark {{ border: 2px solid #161616; }}
  .box b {{ color: #000; }}
  .page2 {{ page-break-before: always; }}
  .step {{ border-left: 3px solid #161616; padding: .6mm 0 .6mm 3.2mm; margin-bottom: 1.8mm; }}
  .step b {{ display: block; margin-bottom: .3mm; }}
  .step span {{ font-size: 8.8pt; color: #3c3c3c; }}
  .foot {{ margin-top: 5mm; border-top: 1px solid #dcdcdc; padding-top: 3.5mm; font-size: 8.6pt; color: #5e5e5e; }}
  .m {{ font-size: 9.3pt; line-height: 1.66; }}
  .kv {{ color: #6a6a6a; }}
</style></head><body>

<div class="kicker">LIFE DECISION SIMULATION</div>
<h1>人生决策推演 · 下载与安装</h1>
<p class="lead">把这份 PDF 丢给你的 AI，说一句话，剩下的它自己会办。</p>
<div class="bar"></div>

<div class="sayit">
  <div class="lb">你要说的话（就这一句）</div>
  <div class="big">帮我下载、安装并调用这个 skill</div>
  <p>不用解释地址、不用教它解压、不用管装哪个目录——从第 2 页开始是一份写给 AI 的完整操作手册，
  下载、校验、解压、选目录、装完怎么调、调不出来怎么办、你的工具不支持技能怎么办，全部写在里面，它会自己看自己处理。</p>
</div>

<div class="tag">
  给 AI 的第一句话：如果你就是被用户把这份 PDF 丢过来的一方，<b>直接跳到第 2 页《操作手册》开始执行</b>。
  用户可能只说了一句"帮我下载安装并调用这个 skill"——那已经够了，不要反问用户，不要只做总结，一路做到"调用"这一步为止。
</div>

<div class="urlbox">
  <div class="lb">主下载地址（永久有效 · 冻结在 v1.0.0 版本上，内容永不改变）</div>
  <div class="u">{URL}</div>
  <div class="tip">电脑、手机浏览器打开都会<b>直接开始下载 zip</b>（已实测）。v1.0.0 是冻结版本：以后更新会发 v1.1.0 等新版本，<b>这个地址永远指向这一份文件，不会失效</b>。</div>
</div>

<div class="urlbox" style="border-color:#8d8d8d">
  <div class="lb">备用地址（按顺序试，任何一个都能下到技能）</div>
  <div class="u" style="font-size:8.3pt">
    <div>备一 · 同版本镜像（手机上会先进「下载仓库」页，点下载按钮即可）：<br>{URL_TAG}</div>
    <div>备二 · 最新版（跟随仓库更新，内容可能比 v1.0.0 新）：<br>{URL_MASTER}</div>
    <div>备三 · GitHub 镜像（需能访问 GitHub）：<br>{URL_GH}</div>
  </div>
</div>

<h2>它读不了 PDF 的话，你自己装（三步，两分钟）</h2>
<div class="step"><b>第一步 · 下载</b><span>复制上面那串地址到浏览器打开，会得到一个 zip。Windows 上如果提示"不常下载"，点"保留"。</span></div>
<div class="step"><b>第二步 · 解压到技能目录</b><span>解压出来通常是一层 <span class="mono">life-decision-simulation-master</span> 文件夹，<b>把里面那层整个文件夹</b>放进去，重命名成 <span class="mono">life-decision-simulation</span>：<br>
  WorkBuddy → <span class="mono">C:\\Users\\你的用户名\\.workbuddy\\skills\\</span><br>
  Claude Code / 桌面版 → <span class="mono">C:\\Users\\你的用户名\\.claude\\skills\\</span></span></div>
<div class="step"><b>第三步 · 确认结构对</b><span>放好之后，路径应该是 <span class="mono">skills\\life-decision-simulation\\SKILL.md</span>——<b>SKILL.md 必须直接在这一层</b>，不要再套一层文件夹，这是最常见的错。</span></div>

<div class="box" style="margin-top:4.5mm">
  <b>装完怎么知道成了：</b>发「我想辞职回老家，收入得减半，你说我该走吗？」<br>
  正常反应是：先用一句话重述你的情况，然后<b>只问一个问题</b>（比如"老家那边工作定了吗"），问完等你答。<br>
  如果它当场甩你一堆建议，说明没装上，回去检查第三步。<br>
  <span class="kv">（技能是在对话开始时加载的，刚装完这一轮可能调不出来——开一个新对话再说就正常了。）</span>
</div>

<div class="page2">
  <h2>操作手册 · 给 AI（用户把这份 PDF 丢给你时，按此执行）</h2>
  <p class="m">任务：把 <b>life-decision-simulation（人生决策推演）</b> 装到本机技能目录，<b>并真的调用一次</b>。
  用户大概只说了"帮我下载安装并调用这个 skill"，其余细节全在下面，<b>不要反问用户</b>，按顺序做完。
  只有落到第七节的硬阻塞时才找用户。</p>

  <h3>一、下载（四个源按顺序试，最多试 8 次）</h3>
  <ul class="m">
    <li>主源（永久冻结文件，内容永不改变）：<span class="mono">{URL}</span></li>
    <li>备一 · Gitee tag 归档（同一版本，手机 UA 可能拿到 HTML 落地页——那是给浏览器看的，换成桌面 UA 或从 HTML 里解析下载链接即可）：<span class="mono">{URL_TAG}</span></li>
    <li>备二 · Gitee 最新版（跟随仓库更新）：<span class="mono">{URL_MASTER}</span></li>
    <li>备三 · GitHub 发行版（国内可能连不上，能连就用）：<span class="mono">{URL_GH}</span></li>
    <li>有命令行：<span class="mono">curl -L --retry 3 -o lds.zip "&lt;地址&gt;"</span>；Windows PowerShell：<span class="mono">Invoke-WebRequest -Uri "&lt;地址&gt;" -OutFile lds.zip -MaximumRedirection 10</span>；都没有用 <span class="mono">python -c "import urllib.request;urllib.request.urlretrieve('&lt;地址&gt;','lds.zip')"</span></li>
    <li>没有命令行环境：用你的浏览器/网页抓取工具打开地址保存文件，或读取文件内容。</li>
    <li><b>下载判定</b>：文件头应是 <span class="mono">PK</span>，大小 30KB–2MB。若拿到的是 <span class="mono">&lt;html</span> 开头，说明被重定向到网页 → 换下一个源重试。</li>
    <li>失败就换源重试，间隔 2s / 5s / 10s 递增，别一次失败就放弃，也别把"网络错误"直接当结论汇报。</li>
    <li>四个源任选其一即可，<b>内容等价</b>（主源和备三是同一份冻结文件；备二可能略新，一样能用）。</li>
  </ul>

  <h3>二、解压（不依赖特定工具）</h3>
  <ul class="m">
    <li>优先 <span class="mono">unzip -q lds.zip -d lds_tmp</span>；Windows 用 <span class="mono">Expand-Archive lds.zip -DestinationPath lds_tmp -Force</span>；都没有用 <span class="mono">python -c "import zipfile;zipfile.ZipFile('lds.zip').extractall('lds_tmp')"</span>。</li>
    <li>解压后在 <span class="mono">lds_tmp</span> 里找 <b>含 SKILL.md 的那一层目录</b>（通常叫 <span class="mono">life-decision-simulation-master/</span>），它就是技能根目录；若 zip 本身是扁平的（SKILL.md 直接在最外层），就把整个 <span class="mono">lds_tmp</span> 当技能根目录。</li>
    <li>把这个根目录重命名/复制为 <span class="mono">life-decision-simulation</span>。</li>
  </ul>

  <h3>三、装到哪儿（自己探测，不要问用户）</h3>
  <ul class="m">
    <li>按顺序探测本机：<span class="mono">~/.workbuddy/</span> → <span class="mono">~/.claude/</span> → <span class="mono">~/.codex/</span> → 你当前运行环境的配置根目录里有没有 <span class="mono">skills</span> 目录。</li>
    <li>命中哪个就把技能放进哪个的 <span class="mono">skills/life-decision-simulation/</span>（目录不存在就创建）。<b>命中多个就都装</b>，反正文件很小。</li>
    <li>一个都没命中：优先创建 <span class="mono">~/.workbuddy/skills/</span> 装进去（这是用户发这份文件时用的工具）；如果你自己明确是别的客户端，装它自己的 skills 目录。</li>
    <li>最终结构必须长这样：<br>
      <span class="mono">skills/life-decision-simulation/SKILL.md</span><br>
      <span class="mono">skills/life-decision-simulation/references/提问总库.md</span><br>
      <span class="mono">skills/life-decision-simulation/references/示范_北京回老家_完整报告.md</span></li>
  </ul>

  <h3>四、校验（这四项跑完才算装完）</h3>
  <ol class="m">
    <li>树结构对：上面三个文件都在，SKILL.md 不在多套的一层里。</li>
    <li>frontmatter 对：SKILL.md 首行是 <span class="mono">---</span>，里面有 <span class="mono">name: life-decision-simulation</span>。</li>
    <li>内容全：SKILL.md 含"六格体检""四位顾问""翻转力"；<span class="mono">提问总库.md</span> 含"第一格"…"第六格"；示范报告含"六问实录"。</li>
    <li>把安装绝对路径 + 这四项结果记下来，第六节回执要用。<b>任何一项不过，回去修，不要带着残缺汇报"已安装"。</b></li>
  </ol>

  <h3>五、调用（重点：调不出来不等于装失败）</h3>
  <div class="box dark">
    <b>先看这一条，否则你会误判：</b>技能清单是<b>在对话开始时加载</b>的。你刚写进磁盘的文件，<b>当前这一轮对话里很可能还不在你的技能列表里</b>——这是正常机制，<b>不是安装失败</b>，绝对不要对用户说"安装失败/找不到技能"。
  </div>
  <ul class="m">
    <li><b>本轮的调用方式：直接把 SKILL.md 当你的操作手册来执行。</b>读全文，然后严格按它走：
      ①先做六格体检，<b>第一句只做两件事——用一句话重述用户的情况，然后只问一个问题</b>，问完停下等他答；
      ②六格问全后，四位顾问依次上场（马斯克第一性原理拆解 → 乔布斯减法取舍 → 芒格逆向算长期 → 王阳明致良知照内心）；
      ③用翻转力排序给结论，四步有一步没过就明确说"先别做"；④输出《人生决策推演报告》（八节）。
      <b>不要一次把全部内容倒给用户，一次只推进一步。</b></li>
    <li>用户如果在这句话里就给了自己的事（比如"我该不该回老家"），<b>别等，直接用第一问开始推演</b>。</li>
    <li>用户如果只说了那句"帮我安装并调用"，那就<b>拿这一问做演示</b>：「先拿你自己的事试一句——你现在正纠结的那个决定是什么？一句话就行。」</li>
    <li>同时告诉用户：要在客户端里"原生调用"，<b>开一个新对话</b>说「帮我推演一下」或直接说纠结的事就行，技能已经装好了。</li>
  </ul>

  <h3>六、回执格式（做完照这个说，别写小作文）</h3>
  <div class="box">
    ✅ 已安装到：<span class="mono">&lt;绝对路径&gt;</span><br>
    ✅ 校验：SKILL.md ✓ ／ 提问总库 ✓ ／ 示范报告 ✓ ／ frontmatter ✓<br>
    ▶ 现在就能用：直接说你的决定（例：我在北京做运营五年，想回老家但收入减半，女朋友还在异地，该不该走）<br>
    ▶ 若你的客户端没立刻识别到新技能：<b>开一个新对话</b>，说"帮我推演一下"即可。
  </div>

  <h3>七、遇到这几种情况怎么自己解决（别问用户，按表处理）</h3>
  <ul class="m">
    <li><b>四个地址都下不动</b>：可能是网络受限。改用你能访问的镜像/代理重试；仍不行，才请用户手动下载第 1 页主地址的 zip，然后把文件拖给你，你从第二节继续。</li>
    <li><b>解压失败/文件损坏</b>：删掉重下一次（换备源）；仍失败说明下载被截断，报告实际字节数。</li>
    <li><b>没有写权限</b>：改写到用户可写目录（如桌面同级目录），把路径明确告诉用户，并给出"手动移动到 skills 目录"的一行命令。</li>
    <li><b>你的运行环境根本没有文件系统</b>（纯网页聊天 AI，不能写文件）：<b>降级方案</b>——把 SKILL.md 全文作为"自定义指令 / 系统提示 / 知识库文件"粘贴进去，然后按第五节的方式直接开始推演；并告诉用户"我这边没法装到磁盘，已用等效方式启用，你换到支持技能的客户端（WorkBuddy / Claude）可以正规安装"。</li>
    <li><b>用户的客户端不支持"技能"这个概念</b>：同上降级，别硬装到乱七八糟的地方。</li>
    <li><b>磁盘上已经有同名技能</b>：先把旧的移到 <span class="mono">life-decision-simulation.bak</span> 再装，装完告诉用户备份在哪。</li>
  </ul>

  <h3>八、不要做的事</h3>
  <ul class="m">
    <li>不要只写一句"我看过这份文档了"就结束——<b>没有落地文件就等于没装</b>。</li>
    <li>不要把 SKILL.md 改名、不要翻译成中文文件名、不要漏掉 references/（示范案例和 48 问总库是这个技能最值钱的部分）。</li>
    <li>不要因为"当前会话调不到技能"就判定失败（见第五节）。</li>
    <li>不要把"网络错误""权限不足"当成最终结论丢给用户，先按第七节处理。</li>
    <li>不要在推演时一口气输出全部六格 + 四位顾问——这个技能的规矩是一次只问一个问题。</li>
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
