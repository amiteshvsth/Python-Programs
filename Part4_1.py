import pylab as pl

class Interest:
    def __init__(self, principle, rate, time):
        self.principle = principle
        self.rate = rate
        self.time = time
        
    def simple_interest(self):
        return self.principle * self.rate * self.time
    
    def compound_interest(self):
        return self.principle * ((1 + self.rate)**self.time - 1)
    
    def plot_interest(self):
        years = range(1, self.time+1)
        simple_interest_values = [self.simple_interest() for year in years]
        compound_interest_values = [self.compound_interest() for year in years]
        
        pl.plot(years, simple_interest_values, label='Simple Interest')
        pl.plot(years, compound_interest_values, label='Compound Interest')
        
        pl.title('Interest Comparison')
        pl.xlabel('Years')
        pl.ylabel('Interest')
        pl.legend()
        pl.show()

# example usage
i = Interest(10000, 0.05, 10)
i.plot_interest()
