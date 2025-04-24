from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Connect to Edge via remote debugging (make sure Edge is running with port 9222)
    browser = p.chromium.connect_over_cdp("http://localhost:9222")

    # Use first context and page
    context = browser.contexts[0]
    page = context.pages[0]

    print("🔍 Extracting all hyperlinks from:", page.url)

    # Get all anchor elements
    links = page.query_selector_all("a")

    print(f"🔗 Found {len(links)} links:\n")

    for i, link in enumerate(links, 1):
        text = link.text_content().strip()
        href = link.get_attribute("href")
        print(f"{i:02d}. Text: {text or '[no text]'}\n    URL: {href}\n")
