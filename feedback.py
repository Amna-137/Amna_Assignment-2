class Feedback:
    """ Feedback class to manage guest reviews and comments."""

    def __init__(self, booking, rating=None):
        self.__booking = booking
        self.__rating = rating
        self.__comments = []

    # Getter methods
    def get_booking(self):
        return self.__booking

    def get_rating(self):
        return self.__rating

    def get_comments(self):
        return self.__comments

    # Setter methods
    def set_rating(self, rating):
        if 1 <= rating <= 5:
            self.__rating = rating


    def submit_feedback(self, rating, comment=None):
        """Submit new feedback"""
        if 1 <= rating <= 5:
            self.__rating = rating
            if comment:
                self.__comments.append(comment)
            print(f"Feedback submitted: Rating {rating}/5")
            return True
        else:
            print("Invalid rating (must be 1-5)")
            return False

    def view_feedback(self):
        """View submitted feedback"""
        if self.__rating:
            comments_str = " | ".join(self.__comments) if self.__comments else "No comments provided"
            return f"Rating: {self.__rating}/5 - Comments: {comments_str}"
        else:
            return "No feedback submitted yet"

    def add_comment(self, comment):
        """Add comment to existing feedback"""
        self.__comments.append(comment)
        print("Comment added")
        return True

    def __str__(self):
        if self.__rating:
            return f"Feedback: Rating {self.__rating}/5, Comments: {len(self.__comments)}"
        else:
            return "Feedback: Not submitted yet"