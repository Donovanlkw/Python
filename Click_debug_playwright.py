from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Connect to manually launched Edge (debug mode on port 9222)
    browser = p.chromium.connect_over_cdp("http://localhost:9222")

    # Use existing context and page (first tab)
    context = browser.contexts[0]
    page = context.pages[0]

    print(f"🖥️ Monitoring tab: {page.url}")

    # Wait for the link with text "abc" to appear (anchor tag <a>)
    print("🔍 Waiting for link with text 'abc' to appear...")
    page.wait_for_selector("a:has-text('Farnborough')", timeout=0)

    # Click the link once it appears
    print("✅ Found link. Clicking it...")
    page.click("a:has-text('Farnborough')")

    print("🖱️ Link clicked.")
