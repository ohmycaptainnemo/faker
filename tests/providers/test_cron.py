from faker.providers.cron import Provider as CronProvider
from faker.providers.cron.en_US import Provider as EnUsCronProvider

class TestCronProvider:
    """Test cron provider methods"""
    
    def test_mastercard(self, faker):
        provider = CronProvider(faker)
        print(provider._create_random_integer_range([0,59]))
