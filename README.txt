# feedback
It allows users of a web-app to report feedback and categorize it as "feature reqeust", "question", and "bug".

## Setup
There is a search field that allows one to search the content of text field
```mysql
create fulltext index description_index on feedback_feedback(description);
create fulltext index summary_index on feedback_feedback(summary);
```