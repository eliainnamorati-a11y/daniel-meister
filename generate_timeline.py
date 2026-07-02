import json

events = [
    {"date": "Geburt & frühe Kindheit", "text": "Geboren in England, wo mein Vater damals beruflich tätig war."},
    {"date": "Kindheit – bis 13 Jahre", "text": "Aufgewachsen in Stuttgart (Deutschland). Frühe Prägung durch ein internationales familiäres Umfeld mit schweizerisch-bernischen und peruanischen Wurzeln. Schulisch übersprang ich die 4. Klasse. Parallel dazu intensive sportliche Förderung im Fussball und Tennis."},
    {"date": "Jugendjahre", "text": "Rückkehr in die Schweiz mit 13 Jahren. Abschluss der Matura an der École Moser in Nyon (VD)."},
    {"date": "Studium – USA & Italien", "text": "Bachelor am Babson College in Wellesley, Massachusetts (USA). Während drei Jahren Mitglied des Varsity Tennis Teams in der NCAA Division III. Austauschsemester an der Università Bocconi in Mailand."},
    {"date": "2018", "text": "Kennenlernen meiner Verlobten Elia während des Studiums in den USA."},
    {"date": "Seit 2019", "text": "Einstieg bei der Silverpine AG, unserem Familienunternehmen im Finanz- und Immobilienbereich."},
    {"date": "2022", "text": "Praktikum bei Comgest Asset Management in Paris im Bereich Aktienanalyse und Portfoliomanagement."},
    {"date": "2023", "text": "Abschluss des Masters in Vermögensverwaltung an der Université de Genève.<br>Vollständiger Eintritt in die operative Tätigkeit bei Silverpine AG."},
    {"date": "Seit 2023", "text": "Verantwortlich für die Immobilienentwicklung der Silverpine AG in der Schweiz sowie für das Finanzportfolio und den Investmentfonds Fortis Capital Sàrl in Luxemburg."},
    {"date": "April 2024", "text": "Kandidat bei den Gemeinderatswahlen in Ennetbürgen. Mit 567 Stimmen ein starkes Resultat als neuer Kandidat erzielt, der Einzug in den Gemeinderat blieb jedoch knapp aus."},
    {"date": "2024", "text": "Wahl zum Vizepräsidenten der SVP Ennetbürgen durch die Generalversammlung der Ortspartei."},
    {"date": "Ende 2024", "text": "Mitgründung der IG Dorfzukunft Ennetbürgen. Tätigkeit im Vorstand und als Kassier. Ziel der überparteilichen Interessengemeinschaft ist es, als Bindeglied zwischen Bevölkerung und Gemeinderat zu wirken."},
    {"date": "Juni 2025", "text": "Wahl in den Vorstand der SVP Nidwalden (Finanzen – Ressort) der Kantonalpartei."},
    {"date": "November 2025", "text": "Nomination als Landratskandidat der SVP Ennetbürgen."},
    {"date": "8. März 2026", "text": "Wahl mit 603 Stimmen in den Landrat des Kantons Nidwalden."},
    {"date": "24. Juni 2026", "text": "Bestätigung durch den Landrat als Mitglied der Finanzkommission des Kantons Nidwalden."}
]

html = """          <div class="about-text">
            <p style="font-family: var(--font-display); font-style: italic; font-size: 2rem; color: var(--primary); margin-bottom: 2rem; line-height: 1.3;"><span class="text-highlight scroll-reveal">„Heute lebe und arbeite ich in Nidwalden – einem Ort, der für mich Heimat, Verantwortung und Zukunft bedeutet.“</span></p>
            <p class="scroll-reveal">Die Wurzeln der Familie meines Vaters reichen zurück ins ländliche Emmental im Kanton Bern, nach Sumiswald. Dank meiner Mutter mit peruanischen Wurzeln bin ich von klein auf von verschiedenen, sich ergänzenden Kulturen, Wertegerüsten und Sprachen geprägt.</p>
            <p class="scroll-reveal" style="margin-top: 1rem;"><span class="text-highlight">Die Kombination aus internationalen Erfahrungen, starken familiären Wurzeln und meiner Verbundenheit zur Schweiz prägt mein Denken und Handeln – beruflich wie politisch.</span></p>
          </div>
        </div>

        <div class="timeline-container">
          <div class="timeline">
"""

for i, event in enumerate(events):
    align = "left" if i % 2 == 0 else "right"
    html += f"""            <div class="timeline-item {align} scroll-reveal">
              <div class="timeline-content">
                <div class="timeline-date">{event['date']}</div>
                <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=2070&auto=format&fit=crop" alt="Timeline Event {i+1}" class="timeline-img">
                <p>{event['text']}</p>
              </div>
            </div>
"""

html += """          </div>
        </div>"""

with open("/Users/eliainnamorati/Desktop/daniel-meister-website/timeline_snippet.html", "w") as f:
    f.write(html)
