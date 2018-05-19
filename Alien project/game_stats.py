class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
