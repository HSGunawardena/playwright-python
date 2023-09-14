class ABTestingPage:
    def __init__(self, page):
        self.page = page
        self.ab_testing_page_heading = page.get_by_role("heading", name="A/B Test Variation 1")

