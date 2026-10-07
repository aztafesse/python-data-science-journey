import numpy as np

# Task 1 - Basic random
print("\n --- Task 1 - Basic random ---")
rng = np.random.default_rng(seed=42)
print(f"5 random floats: {rng.random(5)}")
print(f"5 random interger: {rng.integers(1,101,5)}")
print(f"3x4 array of random integers: \n{rng.integers(0,10,(3,4))}")

# Task 2 - Reproducibility
print("\n --- Task 2 - Reproducibility ---")
rng1 = np.random.default_rng(seed=123)
rng2 = np.random.default_rng(seed=123)
print(f"---Seeded---\nSet 1 : \n{rng1.random(5)}")
print(f"Set 2 : \n{rng2.random(5)}")
rng_a = np.random.default_rng()
rng_b = np.random.default_rng()
print(f"---Unseeded---\nSet 1: \n{rng_a.random(5)}")
print(f"Set 2: \n{rng_b.random(5)}")

# Task 3 - Normal distribution
print("\n --- Task 3 - Normal distribution ---")
rng = np.random.default_rng()
pop = 10000
set1 = rng.normal(50,10,pop)
set1_mean = set1.mean()
set1_std = set1.std()
print(f"Mean: {set1_mean:.4f} and Standad deviation: {set1_std:.4f}")
std1 = set1[(set1>(set1_mean-set1_std)) & (set1< (set1_mean+set1_std))]
print(f"Number of samples within 1 standard deviation of mean: {len(std1)}, around: {len(std1)*100/pop} % of population")
std2 = set1[(set1>=(set1_mean-2*set1_std)) & (set1<=(set1_mean+2*set1_std))]
print(f"Number of samples within 2 standard deviation of mean: {len(std2)}, around :{len(std2)*100/pop} % of population")

# Task 4 - Random choice
print("\n --- Task 4 - Random choice ---")
fruits = np.array(["apple", "banana", "cherry", "date", "elderberry"])
rng = np.random.default_rng()
print(f"Selection of 3 random fruits with replacement:\n {rng.choice(fruits, size =3)}")
print(f"Selection of 3 random fruits without replacement:\n {rng.choice(fruits, size=3, replace = False)}")
print(f"Selection of 10 random fruits with given prbabilities:\n {rng.choice(fruits, size=10, p=[0.5, 0.2, 0.15, 0.1, 0.05])}")

# Task 5 - Dice simulation
print("\n --- Task 5 - Dice simulation ---")
rng = np.random.default_rng()
rolls = rng.integers(1,7,(10000,2))
sum_dice = rolls.sum(axis=1)
print(np.unique(sum_dice,return_counts=True))
p_7 = (sum_dice == 7).mean()
print(f"P(7) is {p_7:.4f}")

# Task 6 - Coin flips
print("\n --- Task 6 - Coin flips ---")
rng = np.random.default_rng()
flip_count = 1000
rolls = rng.integers(0,2,flip_count)
print(f"Numbers of heads on fair coin: {rolls[rolls==1].sum()}")
print(f"Fraction of heads on fair coin: {(rolls[rolls==1].sum()/flip_count):.2f}")
rolls = rng.choice([0,1],size =flip_count,p=[0.3, 0.7])

print(f"Number of heads on biased coin: {rolls[rolls==1].sum()}")
print(f"Fraction of heads on biased coin: {rolls[rolls==1].sum()/flip_count}")

# Task 7 - Monte Carlo pi
print("\n --- Task 7 - Monte Carlo pi ---")
rng = np.random.default_rng(seed=42)
n = 1000000
x = rng.uniform(-1,1,n)
y = rng.uniform(-1,1,n)
r2 = x**2+y**2
print(f" Number of points in the unit circle: {len((r2[r2<=1]))}")
print(f" Estipmation of pi: {4*(len(r2[r2<=1])/n):.5f}")

test = (10000, 100000, 1000000)
accu = []
k=0
for i in test:
    rng = np.random.default_rng(42)
    n = i
    x = rng.uniform(-1,1,i)
    y = rng.uniform(-1,1,i)
    r2 = x**2+y**2
    accu.append(np.pi-4*len(r2[r2<=1])/i)
    k+=1
print(f"Accuracy changes of pi: {accu}")

# Task 8 - Train/test split
print("\n --- Task 8 - Train/test split ---")
arr = np.arange(200)
rng = np.random.default_rng(seed=42)
shuffled = rng.permutation(arr)
train = shuffled[:160]
test = shuffled[160:]
print(f"The first 5 of train: {train[:5]}")
print(f"The first 5 of test: {test[:5]}")
print(f"Confirmation of total: {len(train)+len(test)}")

# Task 9 - Bonus: Birthday paradox
print("\n --- Task 9 - Bonus: Birthday paradox ---")
rng = np.random.default_rng()
bdays = rng.integers(0,365, size=23)

if len(np.unique(bdays))< len(bdays):
    print(f"At least two people share the same birthday")
else:
    print(f"All people have different birthday")

rep = list(range(1000))
pos_test = 0
for i in rep:
    bdays = rng.integers(0,365,23)
    if len(np.unique(bdays))<len(bdays):
        pos_test +=1
print(f"The fraction of trials that had at least one shared birthday is: {pos_test*100/len(rep)}")

