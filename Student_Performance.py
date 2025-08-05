import numpy as np

def create_students(total_students):
    # Generate roll numbers starting from 1 up to total_students
    roll_numbers = np.arange(1, total_students + 1)
    # Create student names like Student_1, Student_2, etc.
    student_names = np.array([f"Student_{num}" for num in roll_numbers])
    return roll_numbers, student_names

def generate_random_scores(total_students, subject_list):
    # Generate random scores between 35 and 99 for each student and each subject
    scores = np.random.randint(35, 100, size=(total_students, len(subject_list)))
    return scores

def show_subject_stats(subject_list, scores):
    # Calculate average, std deviation, max and min for each subject
    averages = np.mean(scores, axis=0)
    std_devs = np.std(scores, axis=0)
    maximums = np.max(scores, axis=0)
    minimums = np.min(scores, axis=0)

    print("Subject-wise Statistics:")
    for i, subject in enumerate(subject_list):
        print(f" {subject}: Avg = {averages[i]:.2f}, Std Dev = {std_devs[i]:.2f}, Max = {maximums[i]}, Min = {minimums[i]}")
    print()

def show_top_students(names, scores, top_count=5):
    # Sum total scores and calculate average per student
    totals = np.sum(scores, axis=1)
    averages = np.mean(scores, axis=1)
    # Get indices that sort totals descending
    sorted_indices = np.argsort(totals)[::-1]

    print(f"Top {top_count} Students:")
    for rank in range(top_count):
        idx = sorted_indices[rank]
        print(f" {rank+1}. {names[idx]} - Total: {totals[idx]}, Average: {averages[idx]:.2f}")
    print()

def show_failed_students(names, scores, pass_mark=40):
    # Find students with any subject score below pass_mark
    failed = scores < pass_mark
    failed_students = names[np.any(failed, axis=1)]

    print(f"Students who failed in at least one subject: {len(failed_students)}")
    # Show only first 5 failed students
    for student in failed_students[:5]:
        print(f" - {student}")
    if len(failed_students) > 5:
        print(" ...")
    print()

def best_and_worst_subjects(subject_list, scores):
    # Calculate average scores for subjects
    averages = np.mean(scores, axis=0)
    best = np.argmax(averages)
    worst = np.argmin(averages)

    print(f"Best subject: {subject_list[best]} with avg score {averages[best]:.2f}")
    print(f"Worst subject: {subject_list[worst]} with avg score {averages[worst]:.2f}")
    print()

def main():
    total_students = 100
    subjects = np.array(["Math", "Physics", "Chemistry", "English", "CS"])

    rolls, names = create_students(total_students)
    scores = generate_random_scores(total_students, subjects)

    print("=== Student Performance Report ===")
    print(f"Total Students: {total_students}")
    print(f"Subjects: {', '.join(subjects)}\n")

    show_subject_stats(subjects, scores)
    show_top_students(names, scores, top_count=5)
    show_failed_students(names, scores, pass_mark=40)
    best_and_worst_subjects(subjects, scores)

    print("=== End of Report ===")

if __name__ == "__main__":
    main()
