class HomePage:
    def __init__(self, page):
        self.page = page
        self.ab_testing_link = page.get_by_role("link", name="A/B Testing")

