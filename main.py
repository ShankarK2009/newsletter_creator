import datetime
from modules.headlines import get_headlines
from modules.sports_results import sports
from modules.tech import tech
from modules.science import science
import minify_html
import css_inline

headlines = None
soccer, bball, madness = None, None, None
tech_res = None
news = None
html_code = ""

def headlines_code(headlines_slider):
    global headlines
    headlines = get_headlines(headlines_slider)

    hlines_code = """
            <section class="headlines margin-top">
                <p class="large margin-bottom">Headlines</p>
                <div class="table">
                    <table>
"""

    num = 0
    hlines_code += "<tr>"
    for i, card in enumerate(headlines, 1):
        card = f"""
                            <td>
                                <div class="card">
                                    <img src="{card[0]}" alt="" class="thumbnail">
                                    <p class="medium bold small-margin-bottom">{card[1]}</p>
                                    <p class="small margin-bottom">{card[2]}</p>
                                    <a href="{card[3]}" class="small">Read More</a>
                                </div>
                            </td>
            """
        hlines_code += card
        num += 1
        
        if num % 2 == 0 and i != len(headlines):
            hlines_code += "</tr><tr>"

    hlines_code += "</tr></table></div></section>"
    return hlines_code

def sports_code(sports_slider):
    global soccer
    global bball
    global madness
    soccer, bball, madness = sports(sports_slider)

    sports_code = """
            <section class="sports margin-top">
                <p class="large">Sports</p>
                <p class="medium-large margin-top margin-bottom">Soccer (PL, La Liga, UCL)</p>
                <div class="table">
                    <table>
                    

    """

    num = 0
    sports_code += "<tr>"

    for i, match in enumerate(soccer, 1):
        if match[5] == "N/A":
            card = f"""
                <td class="noScore">
                    <div class="sportCard">
                        <table>
                            <tr>
                                <td>
                                    <div class="team">
                                        <img src="{match[2]}" alt="" class="logo">
                                        <p class="small">{match[0]}</p>
                                    </div>
                                </td>
                                <td><p class="medium-large">Scheduled</p></td>
                                <td>
                                    <div class="team">
                                        <img src="{match[3]}" alt="" class="logo">
                                        <p class="small">{match[1]}</p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </div>
                </td>
            """
        else:
            card = f"""
                <td class="score">
                    <div class="sportCard">
                        <table>
                            <tr>
                                <td>
                                    <div class="team">
                                        <img src="{match[2]}" alt="" class="logo">
                                        <p class="small">{match[0]}</p>
                                    </div>
                                </td>
                                <td><p class="large">{match[4]}</p></td>
                                <td><p class="large">-</p></td>
                                <td><p class="large">{match[5]}</p></td>
                                <td>
                                    <div class="team">
                                        <img src="{match[3]}" alt="" class="logo">
                                        <p class="small">{match[1]}</p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </div>
                </td>
            """
        
        sports_code += card
        num += 1
        
        if num % 2 == 0 and i != len(soccer):
            sports_code += "</tr><tr>"

    sports_code += "</tr>"
            
    sports_code += """
                </table>
                </div>
                <br>
                <p class="medium-large margin-top margin-bottom">NBA</p>
                <div class="table">
                <table>
"""            

    num = 0
    sports_code += "<tr>"

    for i, match in enumerate(bball, 1):
        if match[5] == "N/A":
            card = f"""
                <td class="noScore">
                    <div class="sportCard">
                        <table>
                            <tr>
                                <td>
                                    <div class="team">
                                        <img src="{match[2]}" alt="" class="logo">
                                        <p class="small">{match[0]}</p>
                                    </div>
                                </td>
                                <td><p class="medium-large">Scheduled</p></td>
                                <td>
                                    <div class="team">
                                        <img src="{match[3]}" alt="" class="logo">
                                        <p class="small">{match[1]}</p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </div>
                </td>
            """
        else:
            card = f"""
                <td class="score">
                    <div class="sportCard">
                        <table>
                            <tr>
                                <td>
                                    <div class="team">
                                        <img src="{match[2]}" alt="" class="logo">
                                        <p class="small">{match[0]}</p>
                                    </div>
                                </td>
                                <td><p class="large">{match[4]}</p></td>
                                <td><p class="large">-</p></td>
                                <td><p class="large">{match[5]}</p></td>
                                <td>
                                    <div class="team">
                                        <img src="{match[3]}" alt="" class="logo">
                                        <p class="small">{match[1]}</p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </div>
                </td>
            """
        
        sports_code += card
        num += 1
        
        if num % 2 == 0 and i != len(soccer):
            sports_code += "</tr><tr>"

    sports_code += "</tr>"

    sports_code += """
                </table>
                </div>
                <br>
                <p class="medium-large margin-top margin-bottom">March Madness</p>
                <div class="table">
                <table>
    """

    num = 0
    sports_code += "<tr>"

    for i, match in enumerate(madness, 1):
        if match[5] == "N/A":
            card = f"""
                <td class="noScore">
                    <div class="sportCard">
                        <table>
                            <tr>
                                <td>
                                    <div class="team">
                                        <img src="{match[2]}" alt="" class="logo">
                                        <p class="small">{match[0]}</p>
                                    </div>
                                </td>
                                <td><p class="medium-large">Scheduled</p></td>
                                <td>
                                    <div class="team">
                                        <img src="{match[3]}" alt="" class="logo">
                                        <p class="small">{match[1]}</p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </div>
                </td>
            """
        else:
            card = f"""
                <td class="score">
                    <div class="sportCard">
                        <table>
                            <tr>
                                <td>
                                    <div class="team">
                                        <img src="{match[2]}" alt="" class="logo">
                                        <p class="small">{match[0]}</p>
                                    </div>
                                </td>
                                <td><p class="large">{match[4]}</p></td>
                                <td><p class="large">-</p></td>
                                <td><p class="large">{match[5]}</p></td>
                                <td>
                                    <div class="team">
                                        <img src="{match[3]}" alt="" class="logo">
                                        <p class="small">{match[1]}</p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </div>
                </td>
            """
        
        sports_code += card
        num += 1
        
        if num % 2 == 0 and i != len(soccer):
            sports_code += "</tr><tr>"

    sports_code += "</tr>"
    sports_code += """
                    </table>
                    </div>
                </div>
            </section>
    """

    return sports_code

def tech_code(tech_slider):
    global tech_res
    tech_res = tech(tech_slider)
    
    tech_code = """
            <section class="technology margin-top">
                <p class="large margin-bottom">Technology</p>
                <div class="table">
                    <table>
    """

    num = 0
    tech_code += "<tr>"
    for i, card in enumerate(tech_res, 1):
        card = f"""
                            <td>
                                <div class="card">
                                    <img src="{card[0]}" alt="" class="thumbnail">
                                    <p class="medium bold small-margin-bottom">{card[1]}</p>
                                    <p class="small margin-bottom">{card[2]}</p>
                                    <a href="{card[3]}" class="small">Read More</a>
                                </div>
                            </td>
            """
        tech_code += card
        num += 1
        
        if num % 2 == 0 and i != len(headlines):
            tech_code += "</tr><tr>"

    tech_code += "</tr></table></div></section>"
    return tech_code

def science_code(science_slider):
    global news
    news = science(science_slider)

    science_code = """
            <section class="science margin-top">
                <p class="large margin-bottom">Science</p>
                <div class="table">
                    <table>
    """

    num = 0
    science_code += "<tr>"
    for i, card in enumerate(news, 1):
        card = f"""
                            <td>
                                <div class="card">
                                    <img src="{card[0]}" alt="" class="thumbnail">
                                    <p class="medium bold small-margin-bottom">{card[1]}</p>
                                    <p class="small margin-bottom">{card[2]}</p>
                                    <a href="{card[3]}" class="small">Read More</a>
                                </div>
                            </td>
            """
        science_code += card
        num += 1
        
        if num % 2 == 0 and i != len(news):
            science_code += "</tr><tr>"

    science_code += "</tr></table></div></section>"
    return science_code    

def footer_code(name):
     footer = """
            <footer class="footer margin-top">
                <hr>
                <br>
                <p class="small">Copyright © The Weekly Pulse 2025, All rights reserved</p>
                <br>
                <p class="small">About <a class="lakshan" href="lakshansuresh.netlify.app">"""+name+"""</a></p>
                <br>
                <hr class="margin-bottom">
            </footer>
    """
     return footer

def create(name, headlines_slider, sports_slider, tech_slider, science_slider, inline_css, minify):
    global html_code
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>The Weekly Pulse</title>
    </head>
    <style>
        @import "https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap";

        :root {
            --font1: "DM Sans", "Helvetica";
            --font2: "Work Sans", "Arial";
        }
        
        * {
            margin: 0;
            padding: 0;
            font-size: 100%
        }

        article {
            width: 80%;
            margin: auto
        }

        .large {
            font-family: var(--font1);
            color: black;
            font-size: 30px;
            font-weight: 700
        }

        .medium-large {
            font-family: var(--font1);
            font-size: 20px;
        }

        .small {
            font-family: var(--font2);
            color: #000;
            font-size: 15px;
        }

        .medium {
            font-family: var(--font2);
            font-size: 20px;
        }

        .littleSpace {
            padding: 20px
        }

        .margin-top {
            margin-top: 20px
        }

        .margin-bottom {
            margin-bottom: 20px
        }

        .small-margin-top {
            margin-top: 5px
        }

        .small-margin-bottom {
            margin-bottom: 5px
        }

        .bold {
            font-weight: 700
        }

        .card {
            border: 3px solid black;
            border-radius: 10px;
            padding: 25px 15px;
        }

        img {
            border-radius: 10px;
            width: 100%;
        }

        .sports {
            margin-top: 50px;
        }

        a:not(.lakshan) {
            color: #000;
            border: 2px solid black;
            border-radius: 5px;
            padding: 10px;
            text-decoration: none
        }

        .card img {
            object-fit: cover;
            height: 200px;
        }

        .sportCard {
            box-sizing: border-box;
            border: 3px solid black;
            border-radius: 10px;
            width: max-content;
            margin: 5px;
            padding: 10px;
        }

        .sportCard table tr td {
            text-align: center;
            vertical-align: middle;
            /* width: auto; */
            /* height: 120px; */
            padding: 5px
        }

        .team {
            text-align: center;
            /* display: inline-block */
        }

        .team img {
            margin: 0 auto;
            display: block
        }

        .logo {
            width: 50px;
            aspect-ratio: 1 1;
        }

        .footer {
            padding: 20px 0
        }

        .table {
            float: left;
            width: 100%;
            display: block;
        }

        section table tr td {
            padding: 5px;
        }

        .headlines table tr td,
        .technology table tr td,
        .science table tr td {
            display: inline-block;
            max-width: 360px;
            width: 100%;
            vertical-align: top;
        }

        .sports table tr td {
            display: inline-block;
            max-width: 350px;
            /* width: 200px; */
            height: max-content;
        }
    </style>
    <body>
        <article>
            <div class="marginTop newsletterContainer">
                <h1 class="large">The Weekly Pulse</h1>
                <div class="margin-top">
                    <hr>
                    <div class="littleSpace  dateContainer">
                        <p class="medium">"""+datetime.datetime.now().strftime("%B %d, %Y")+"""</p>
                        <p class="small">"""+name+"""</p>
                    </div>
                    <hr>
                </div>
                <div class="margin-top margin-bottom">
                    <p class="medium">Welcome!<br><br>Stay ahead with today’s most important updates—curated just for you. Whether it’s breaking news, thrilling sports results, market-moving finance trends, or groundbreaking science discoveries, we bring you the stories that matter in a clear, concise format.<br><br>Dive in and explore what’s shaping our world right now.<br><br>Happy reading!</p>
                </div>
                <hr>
                
    """

    html_code += headlines_code(headlines_slider)
    html_code += sports_code(sports_slider)
    html_code += tech_code(tech_slider)
    html_code += science_code(science_slider)
    html_code += footer_code(name)

    html_code += """
            </div>
        </article>
    </body>
    </html>
    """

    html_file = open("generated_newsletter.html", "w")

    if inline_css:
        html_code = css_inline.inline(html_code)

    if minify:
        html_code = minify_html.minify(html_code, remove_processing_instructions=True)

    html_code += "</body></head></html>"

    html_file.write(html_code)
    return html_code