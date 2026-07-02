import glob
import re

new_footer_html = """    <!-- Footer -->
    <footer class="footer">
      <div class="footer-cta">
        <h2>Zukunft gemeinsam gestalten.</h2>
      </div>
      <div class="footer-container">
        <!-- Column 1: Info -->
        <div class="footer-col">
          <img src="logo%20white.png" alt="Daniel Meister" class="footer-logo">
          <p class="footer-mission">Freiheit, Verantwortung und starke Werte &ndash; für ein sicheres und erfolgreiches Nidwalden.</p>
        </div>
        
        <!-- Column 2: Navigation -->
        <div class="footer-col">
          <h3>Navigation</h3>
          <div class="footer-nav">
            <a href="about.html">Wer bin ich?</a>
            <a href="politik.html">Meine Politik</a>
            <a href="aktuelles.html">Aktuelles</a>
            <a href="kontakt.html">Kontakt</a>
          </div>
        </div>

        <!-- Column 3: Contact -->
        <div class="footer-col">
          <h3>Kontakt</h3>
          <p class="footer-address">
            Daniel Meister<br>
            Bürgenstockstrasse 50<br>
            6373 Ennetbürgen
          </p>
          <a href="mailto:daniel.meister@parl-nw.ch" class="footer-email">daniel.meister@parl-nw.ch</a>
          
          <div class="footer-affiliation">
            <img src="SVP_NW_Favicon.png" alt="SVP Nidwalden">
          </div>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p>&copy; 2026 Daniel Meister. Alle Rechte vorbehalten.</p>
        <div class="footer-legal">
          <a href="#">Impressum</a>
          <a href="#">Datenschutz</a>
        </div>
      </div>
    </footer>"""

for filepath in glob.glob("*.html"):
    with open(filepath, "r") as f:
        content = f.read()
    
    # Replace footer
    pattern = re.compile(r'    <!-- Footer -->\n    <footer class="footer">.*?    </footer>', re.DOTALL)
    content = pattern.sub(new_footer_html, content)
    
    # Bump CSS cache
    content = re.sub(r"style\.css\?v=\d+", "style.css?v=44", content)
    
    with open(filepath, "w") as f:
        f.write(content)

print("Updated HTML files.")
