/// main course content
///
/// can be the actual section of a topic
///
/// e.g Quadratic Equations
class CourseContent {
  final int? id;
  final DateTime createdOn;
  final String title;
  final String content;
  final bool isComplete;

  CourseContent({
    this.id,
    required this.createdOn,
    required this.title,
    required this.content,
    this.isComplete = false,
  });
}
