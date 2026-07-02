import re

events = [
    {"date": "1998", "title": "Geburt & frühe Kindheit", "text": "Geboren in England, wo mein Vater zu dieser Zeit beruflich tätig war."},
    {"date": "1999–2011", "title": "Kindheit in Deutschland", "text": "Ich wuchs in Stuttgart, Deutschland, in einem internationalen familiären Umfeld mit schweizerisch-bernischen und peruanischen Wurzeln auf. In der Schule übersprang ich die vierte Klasse. Gleichzeitig erhielt ich eine intensive sportliche Ausbildung im Fußball und Tennis."},
    {"date": "2011–2016", "title": "Jugend & Schulzeit in der Schweiz", "text": "Im Alter von 13 Jahren kehrte ich in die Schweiz zurück und absolvierte meine Sekundarschulzeit an der École Moser in Nyon (VD)."},
    {"date": "2015", "title": "Auslandsaufenthalt in Neuseeland", "text": "Ich verbrachte fünf Monate in Neuseeland, wo ich viel Zeit in der Natur verbrachte und lernte, unabhängig in der Wildnis zu leben – unter anderem durch Jagen, Fischen und Survival-Training. Diese Erfahrung vertiefte meine Wertschätzung für die Natur und stärkte meinen Respekt gegenüber anderen Kulturen, insbesondere durch den Austausch mit Māori und Einheimischen."},
    {"date": "2016–2019", "title": "Studium in den USA & Italien", "text": "Bachelorstudium am Babson College in Wellesley, Massachusetts (USA). Während drei Jahren Mitglied des Varsity-Tennisteams in der NCAA Division III. Zudem absolvierte ich ein Austauschsemester an der Bocconi University in Mailand."},
    {"date": "2018", "title": "Persönlicher Meilenstein", "text": "Während meines Studiums in den USA lernte ich meine Verlobte Elia kennen."},
    {"date": "Seit 2019", "title": "Einstieg bei Silverpine AG", "text": "Eintritt in die <a href=\"https://silverpine.ch\" target=\"_blank\">Silverpine AG</a>, unser Familienunternehmen im Finanz- und Immobiliensektor."},
    {"date": "2022", "title": "Praktikum im Asset Management", "text": "Praktikum bei <a href=\"https://www.comgest.com\" target=\"_blank\">Comgest Asset Management</a> in Paris im Bereich Aktienanalyse und Portfoliomanagement."},
    {"date": "2023", "title": "Masterabschluss & operative Verantwortung", "text": "Masterabschluss in Asset Management an der University of Geneva. Gleichzeitig vollständiger Einstieg in die operative Tätigkeit bei Silverpine AG."},
    {"date": "Seit 2023", "title": "Führungsverantwortung", "text": "Verantwortlich für die Immobilienentwicklung der Silverpine AG in der Schweiz sowie für das Finanzportfolio und den Investmentfonds Fortis Capital Sàrl in Luxemburg."},
    {"date": "April 2024", "title": "Eintritt in die Politik", "text": "Kandidatur bei den Gemeinderatswahlen in Ennetbürgen. Als Neukandidat erzielte ich mit 567 Stimmen ein starkes Resultat und verpasste den Einzug in den Gemeinderat nur knapp."},
    {"date": "2024", "title": "Wahl zum Vizepräsidenten der SVP Ennetbürgen", "text": "Wahl zum Vizepräsidenten der SVP Ennetbürgen durch die Generalversammlung der Ortspartei."},
    {"date": "Ende 2024", "title": "Gesellschaftliches Engagement", "text": "Mitgründer der Interessengemeinschaft Zukunft Dorf Ennetbürgen. Tätigkeit als Vorstandsmitglied und Kassier. Ziel der überparteilichen Interessengemeinschaft ist es, als Bindeglied zwischen Bevölkerung und Gemeinderat zu wirken."},
    {"date": "Juni 2025", "title": "Wahl in den Kantonalvorstand", "text": "Wahl in den Vorstand der SVP Nidwalden im Bereich Finanzen."},
    {"date": "November 2025", "title": "Nomination für den Bezirksrat", "text": "Nomination als Kandidat der SVP Ennetbürgen für den Bezirksrat."},
    {"date": "8. März 2026", "title": "Wahl in den Kantonsrat", "text": "Mit 603 Stimmen in den Kantonsrat Nidwalden gewählt."},
    {"date": "24. Juni 2026", "title": "Berufung in die Finanzkommission", "text": "Bestätigung durch den Regierungsrat als Mitglied der Finanzkommission des Kantons Nidwalden."}
]

html_parts = []
html_parts.append('    <div class="story-wrapper" id="story-wrapper">\n')
html_parts.append('      <div class="story-sticky" id="story-sticky">\n')
html_parts.append('        \n')
html_parts.append('        <div class="story-ruler-container">\n')
html_parts.append('           <div class="story-ruler" id="story-ruler">\n')

n = len(events)
for i, ev in enumerate(events):
    pct = i / (n - 1) * 100
    html_parts.append(f'             <div class="story-ruler-label" style="left: {pct:.2f}%; margin-left: 20px;">{ev["date"]}</div>\n')

html_parts.append('           </div>\n')
html_parts.append('        </div>\n')
html_parts.append('        \n')
html_parts.append('        <div class="story-cards-container">\n')

for i, ev in enumerate(events):
    transform = 'transform: translateY(0);' if i == 0 else ''
    html_parts.append(f'           <div class="story-card" style="{transform}">\n')
    html_parts.append('             <div class="story-card-left">\n')
    html_parts.append(f'               <h2 class="story-title">{ev["title"]}</h2>\n')
    html_parts.append('             </div>\n')
    html_parts.append('             <div class="story-card-right">\n')
    html_parts.append(f'               <p class="story-text">{ev["text"]}</p>\n')
    html_parts.append('             </div>\n')
    html_parts.append('           </div>\n')

html_parts.append('         </div>\n')
html_parts.append('      </div>\n')
html_parts.append('    </div>')

new_timeline_html = "".join(html_parts)

with open('about.html', 'r') as f:
    content = f.read()

# Replace the block
pattern = re.compile(r'    <div class="story-wrapper" id="story-wrapper">.*?    </div>\n', re.DOTALL)
content = pattern.sub(new_timeline_html + "\n", content)

with open('about.html', 'w') as f:
    f.write(content)

print("Updated about.html")
