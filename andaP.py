import subprocess
import os
import json
# 1er étape Le module Node.js  
PUPPETEER_SCRIPT= """
    const puppeteer = requiere ('puppeteer);
    const page = await browser.newPage();

    const siteUrl = process.argv[2];
    
    await page.goto(siteUrl, { waitUntil: 'networkidle2' });
    
    const links = await page.evaluate(() => {
        return Array.from(document.querySelectorAll('a')).map(link => link.href);
    });

    for (const link of links) {
        if (link.startsWith(siteUrl)) {
            try {
                await page.goto(link, { waitUntil: 'networkidle2' });
                console.log('Visited:', link);
            } catch (error) {
                console.error('Error visiting:', link);
            }
        }
    }

    await browser.close();

    console.log(JSON.stringify(links));
})();"""

# 2eme étape Le module Puppeteer

def write_puppeteer_script():
    """Writes the Puppeteer script to a temporary JavaScript file."""
    with open('puppeteer_browse.js', 'w') as f:
        f.write(PUPPETEER_SCRIPT)

def run_puppeteer(url):
    try:
        result = subprocess.run(
            ['node', 'puppeteer_browse.js', url],
            capture_output=True, text=True, check=True
        )
        links = json.loads(result.stdout.splitlines()[-1])
        return links
    except subprocess.CalledProcessError as e:
        print(f"Error running Puppeteer: {e}")
        return []

def clone_site(url, output_dir, links):
    """Clones the site using httrack based on visited links."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 3eme étape Le module httrack command pour coppier les page
    httrack_command = [
        "httrack",
        url,
        "-O", output_dir,
        "--mirror",
        "--robots=0",
        "--depth=3",
        "--disable-security-limits"
    ]

    # Add each link found by Puppeteer as additional starting points
    for link in links:
        httrack_command.extend(["+" + link])

    try:
        subprocess.run(httrack_command, check=True)
        print(f"Successfully cloned {url} to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning site: {e}")

# 4eme module Main
if __name__ == "__main__":
    site_url = "https://www.andapirate.com" 
    output_directory = "Clone_Panda" 

    write_puppeteer_script()
    visited_links = run_puppeteer(site_url)
    clone_site(site_url, output_directory, visited_links)
