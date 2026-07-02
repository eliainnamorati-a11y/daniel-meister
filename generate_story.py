import os

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

html = """        </div>
      </div>
    </section>

    <!-- LimeIQ Style Sticky Scrollytelling Timeline -->
    <div class="story-wrapper" id="story-wrapper">
      <div class="story-sticky" id="story-sticky">
        
        <div class="story-ruler-container">
           <div class="story-ruler" id="story-ruler">
"""

# Generate ruler labels
for i, event in enumerate(events):
    # Position each label based on its index
    left_pos = (i / len(events)) * 100
    # Create short labels for the ruler to avoid overlap
    short_date = event['date']
    if len(short_date) > 15:
        short_date = short_date.split(" ")[0] # Just the first word/year for long ones
    html += f"""             <div class="story-ruler-label" style="left: {left_pos}%; margin-left: 20px;">{short_date}</div>\n"""

html += """           </div>
        </div>
        
        <div class="story-cards-container">
"""

# Generate cards
for i, event in enumerate(events):
    style = "transform: translateY(0);" if i == 0 else ""
    html += f"""           <div class="story-card" style="{style}">
             <div class="story-card-left">
               <h2 class="story-title">{event['date']}</h2>
             </div>
             <div class="story-card-right">
               <p class="story-text">{event['text']}</p>
             </div>
           </div>
"""

html += """        </div>
      </div>
    </div>"""

# Replace in about.html
with open("/Users/eliainnamorati/Desktop/daniel-meister-website/about.html", "r") as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if i == 71: # Line 72 (timeline-container start)
        new_lines.append(html + "\n")
        skip = True
    if i == 190: # Line 191 (after </section>)
        skip = False
        continue # don't append the </section> again since it's in our html snippet
        
    if not skip:
        new_lines.append(line)

with open("/Users/eliainnamorati/Desktop/daniel-meister-website/about.html", "w") as f:
    f.writelines(new_lines)

# Append CSS
css = """
/* LimeIQ Style Sticky Timeline */
.story-wrapper {
  height: 1600vh; /* 100vh per card (16 cards) */
  position: relative;
  background: var(--bg-color);
}
.story-sticky {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: hidden;
  background: var(--bg-color);
}
.story-ruler-container {
  width: 100%;
  height: 60px;
  position: absolute;
  top: 0; left: 0;
  overflow: hidden;
  border-bottom: 1px solid rgba(0,0,0,0.1);
  background: var(--bg-color);
  z-index: 10;
}
.story-ruler {
  height: 100%;
  width: 1600%; /* 100% * 16 items */
  position: absolute;
  top: 0; left: 0;
  background-image: repeating-linear-gradient(to right, transparent, transparent 19px, rgba(0,0,0,0.1) 19px, rgba(0,0,0,0.1) 20px);
  background-position: bottom;
  background-size: 20px 20px;
  background-repeat: repeat-x;
  will-change: transform;
}
.story-ruler-label {
  position: absolute;
  bottom: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
}
.story-cards-container {
  width: 100%;
  height: calc(100vh - 60px);
  margin-top: 60px;
  position: relative;
}
.story-card {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  background: var(--bg-color);
  transform: translateY(100vh); /* Start off-screen */
  will-change: transform;
  box-shadow: 0 -30px 60px rgba(0,0,0,0.03); /* Subtle shadow on top edge */
}
.story-card-left {
  flex: 1;
  padding: 4rem;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}
.story-title {
  font-family: var(--font-display);
  font-size: clamp(3rem, 6vw, 6.5rem);
  font-weight: normal;
  color: var(--text-main);
  line-height: 1.1;
  letter-spacing: -0.02em;
}
.story-card-right {
  flex: 1;
  padding: 4rem 4rem 4rem 0;
  display: flex;
  align-items: center;
}
.story-text {
  font-size: 1.4rem;
  line-height: 1.6;
  color: var(--text-muted);
  max-width: 550px;
}

@media (max-width: 768px) {
  .story-card {
    flex-direction: column;
  }
  .story-card-left {
    padding: 2rem 2rem 0 2rem;
    align-items: flex-end;
  }
  .story-title { 
    font-size: 3rem; 
    text-align: left;
    width: 100%;
  }
  .story-card-right {
    padding: 1rem 2rem 2rem 2rem;
    align-items: flex-start;
  }
  .story-text { font-size: 1.1rem; }
}
"""

with open("/Users/eliainnamorati/Desktop/daniel-meister-website/style.css", "a") as f:
    f.write(css)

# Append JS
js = """
// LimeIQ Sticky Timeline Scroll Logic
document.addEventListener("DOMContentLoaded", () => {
  const wrapper = document.getElementById('story-wrapper');
  const ruler = document.getElementById('story-ruler');
  const cards = document.querySelectorAll('.story-card');
  
  if (wrapper && ruler && cards.length > 0) {
    const numCards = cards.length;
    
    // Use requestAnimationFrame for smooth scrolling
    let ticking = false;
    
    function updateTimeline() {
      const rect = wrapper.getBoundingClientRect();
      
      // Calculate progress from 0 to 1
      // When rect.top == 0, progress = 0
      // When rect.bottom == window.innerHeight, progress = 1
      let progress = -rect.top / (rect.height - window.innerHeight);
      progress = Math.max(0, Math.min(1, progress));
      
      // Move Ruler horizontally. Max move is - (numCards-1)/numCards * 100%
      const maxTranslateX = ((numCards - 1) / numCards) * 100;
      ruler.style.transform = `translate3d(-${progress * maxTranslateX}%, 0, 0)`;
      
      // Translate Cards
      cards.forEach((card, index) => {
        if (index === 0) return; // Base card always stays at 0
        
        const start = (index - 1) / (numCards - 1);
        const end = index / (numCards - 1);
        
        let cardProgress = (progress - start) / (end - start);
        cardProgress = Math.max(0, Math.min(1, cardProgress));
        
        // cardProgress 0 -> 1 maps to translateY 100vh -> 0vh
        const yOffset = 100 - (cardProgress * 100);
        card.style.transform = `translate3d(0, ${yOffset}vh, 0)`;
      });
      
      ticking = false;
    }
    
    // Initial call
    updateTimeline();
    
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(updateTimeline);
        ticking = true;
      }
    });
  }
});
"""

with open("/Users/eliainnamorati/Desktop/daniel-meister-website/main.js", "a") as f:
    f.write(js)
