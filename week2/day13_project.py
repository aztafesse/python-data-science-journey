import numpy as np

print("\n --- Step 1 - Generate the Dataset ---")
# seed for reproducibility
rng = np.random.default_rng(seed=42)

n_students = 500
n_tests = 3 # math, science, english

# Base ability per student: mean 65, std 12
ability = rng.normal(65,12,n_students)

# Subject dificulty adjusment: math +2, science -5, english 0
subject_offsets = np.array([2, -5, 0])

# Generate scores: ability + subject offset + noise
# Shape: (n_studnets, n_tests)
noise = rng.normal(0,8,(n_students, n_tests))
#scores = ability.reshape(-1,1) + subject_offsets+noise
scores = ability[:,np.newaxis] + subject_offsets + noise

# Clip to [0, 100]
scores = np.clip(scores,0,100)

# Introduce missing values: ~3% of scores
missing_mask = rng.random((n_students, n_tests)) < 0.03
scores[missing_mask] = np.nan

print(f"Dataset shape: {scores.shape}")
print(f"First 3 rows:\n{scores[:3]}")
print(f"Missing values: {np.isnan(scores).sum()}")

# Step 2 - Overall Statistics
print(f" --- Step 2 - Overall Statistics ---")
print(f"Mean: {np.nanmean(scores):.2f}")
print(f"Standard deviation: {np.nanstd(scores):.2f}")
print(f"Minimum: {np.nanmin(scores):.2f}")
print(f"Maximum: {np.nanmax(scores):.2f}")

print("==== Per subject Statistics ====")
subjects = ["Math", "Science", "English"]
for i, subject in enumerate(subjects):
    col = scores[:,i]
    print(f"{subject:8s} | mean={np.nanmean(col):6.2f} std= {np.nanstd(col):5.2f} " 
          f"min= {np.nanmin(col):5.2f} max= {np.nanmax(col):5.2f}")

print("==== Per student mean (first 5) ====")
student_means = np.nanmean(scores, axis=1)
print(student_means[:5])

# Step 3 - Filtering & Ranking
print(f" ---- Step 3 - Filtering & Ranking ----")

print("\n=== Students with score above 80 on Math ===")
math_mask = scores[:,0] > 80
print(f"Count: {math_mask.sum()}")
print(f"First 5 math scores above 80: {scores[math_mask,0][0:5]}")

print("\n=== Studnets who scores at least 90 on any test")
any_high  = np.any(scores >=70, axis=1)
high_avg = np.nanmean(scores[any_high],axis=0)
print(f"Count: {any_high.sum()}")
print(f"Average per test of these student: {high_avg}")

print("\n=== Top 10 students by average score ===")
top_idx = np.argsort(student_means)[-10:][::-1]
print(f"Indices: {top_idx}")
print(f"Averages: {student_means[top_idx]}")

print("\n=== Bottom 10 students ===")
bottom_idx = np.argsort(student_means)[:10]
print(f"Indices: {bottom_idx}")
print(f"Averages: {student_means[bottom_idx]}")

# Step 4 - Normilization & Standardization
print(" --- Step 4 - Normilization & Standardization ----")
print("\n=== Min-Max Normalization ===")
col_min = np.nanmin(scores, axis=0)
col_max = np.nanmax(scores, axis=0)
normalized = (scores-col_min)/(col_max-col_min)

print(f"Normalized overall min: {np.nanmin(normalized):.4f}")
print(f"Normalized overall max: {np.nanmax(normalized):.4f}")
print(f"Per-column mins: {np.nanmin(normalized, axis=0)}")
print(f"Per-column maxes: {np.nanmax(normalized, axis=0)}")

print(f"\n=== Z-Score Standardization ===")
col_means = np.nanmean(scores,axis=0)
col_stds = np.nanstd(scores, axis=0)
standardized = (scores-col_means)/col_stds

print(f"Per column means: {np.nanmean(standardized, axis=0)}")
print(f"Per column stds: {np.nanstd(standardized, axis=0)}")


# Step 5 - Correlations Between Subjects
print(" ---- Step 5 - Correlations Between Subjects ----")

complete_mask = ~np.isnan(scores).any( axis=1)
complete_scores = scores[complete_mask]

print(f"Complete rows: {len(complete_scores)} / {n_students}")
#print(complete_scores)

corr = np.corrcoef(complete_scores.T)
print("Correlation Matrix:")
print(np.round(corr,3))

# Step 6 - Pass/Fail Analysis
print("=== Step 6 - Pass/Fail Analysis ===")

pass_threshold = 60

passed = scores >= pass_threshold
passed_no_nan = passed & ~np.isnan(scores)

print(f"Total scores: {scores.size}")
print(f"Passing scores: {passed_no_nan.sum()}")
print(f"Pass rate overall: {passed_no_nan.sum()/(~np.isnan(scores)).sum():.2%}")

print("\nPer-subject pass rate:")
for i, subject in enumerate(subjects):
    col_passed = passed_no_nan[:,i].sum()
    col_total = (~np.isnan(scores[:,i])).sum()
    rate = col_passed/col_total if col_total > 0 else 0
    print(f"{subject:8s}: {rate:.2%}")

# Student who passed all 3 subjects
passed_all = np.all(passed_no_nan, axis =1)
print(f"\nPassed all 3 subjects: {passed_all.sum()}")

# student who failed at least one
fail_any = np.any(~passed_no_nan & ~np.isnan(scores), axis =1)
print(f"Failed at least one: {fail_any.sum()}")
print(np.isnan(scores).sum())

# Step 7 - Simulate an improvement
print("---- Step 7 Simulate an improvement ----")

struggling = student_means < 60
print(f"Students getting tutoring: {struggling.sum()}")

new_scores = scores.copy()
improvement = rng.normal(8, 3, (struggling.sum(), n_tests))
new_scores[struggling] = np.clip(new_scores[struggling] + improvement,0,100)

# Compare
old_avg = np.nanmean(student_means[struggling])
new_avg = np.nanmean(np.nanmean(new_scores, axis =1))

print(f"Before tutoring: mean = {old_avg:.2f}")
print(f"After tutoring: mean = {new_avg:.2f}")
print(f"Improvement: {new_avg-old_avg:+.2f} points")

# Class wide effect
overall_before = np.nanmean(scores)
overall_after = np.nanmean(new_scores)
print(f"\nClass average before: {overall_before}")
print(f"Class average after: {overall_after}")

# Step 8 - Save the results

print(" ---- Step 8 - Save the results ----")
with open("day13_summary.txt", "w") as f:
    f.write("=== Student Performance Analysis ===\n\n")
    f.write(f"Students: {n_students}\n")
    f.write(f"Subjects: {', '.join(subjects)}\n")
    f.write(f"Missing scores: {np.isnan(scores).sum()}\n\n")

    f.write("Overall Statistics:\n")
    f.write(f"  Mean: {np.nanmean(scores):.2f}\n")
    f.write(f"  Std:  {np.nanstd(scores):.2f}\n")
    f.write(f"  Min:  {np.nanmin(scores):.2f}\n")
    f.write(f"  Max: {np.nanmax(scores):.2f}\n\n")

    f.write("Per-Subject Means:\n")
    for i, subject in enumerate(subjects):
        f.write(f"  {subject}:  {np.nanmean(scores[:,i]):.2f}\n")

    f.write(f"\nPass rate (>=60): {passed_no_nan.sum()/(~np.isnan(scores)).sum():.2%}\n")
    f.write(f"Top 10 averages: {student_means[top_idx].round(2).tolist()}\n")

print("\nSummary saved to day13_summary.txt")


