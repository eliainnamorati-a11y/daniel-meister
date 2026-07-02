const fs = require('fs');
const path = '/Users/eliainnamorati/.gemini/antigravity/scratch/daniel-meister-website/';

let indexHtml = fs.readFileSync(path + 'index.html', 'utf8');
let aktuellesHtml = fs.readFileSync(path + 'aktuelles.html', 'utf8');

const latestRegex = /<!-- Latest News Section -->\s*<section id="latest"[\s\S]*?<\/section>/;
const latestMatch = indexHtml.match(latestRegex);

if(latestMatch) {
    const latestContent = latestMatch[0];
    
    // Remove from index
    indexHtml = indexHtml.replace(latestRegex, '');
    fs.writeFileSync(path + 'index.html', indexHtml);
    
    // Replace in aktuelles
    const politicsRegex = /<!-- My Politics Section -->\s*<section id="politics"[\s\S]*?<\/section>/;
    aktuellesHtml = aktuellesHtml.replace(politicsRegex, latestContent);
    
    // Replace titles
    aktuellesHtml = aktuellesHtml.replace('<title>Daniel Meister - Meine Politik</title>', '<title>Daniel Meister - Aktuelles</title>');
    aktuellesHtml = aktuellesHtml.replace('Meine Politik</h1>', 'Aktuelles</h1>');
    
    fs.writeFileSync(path + 'aktuelles.html', aktuellesHtml);
    console.log("Success");
} else {
    console.log("Failed to find latest section");
}
