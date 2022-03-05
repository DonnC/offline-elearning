import 'index.dart';

/// main course content
///
/// can be the actual section of a topic
///
/// e.g Quadratic Equations
class CourseContent {
  final int? id;

  /// created or updated on
  final DateTime? createdOn;
  final Teacher? addedBy;
  final String title;
  final String content;
  final bool isComplete;

  CourseContent({
    this.id,
    this.addedBy,
    this.createdOn,
    required this.title,
    required this.content,
    this.isComplete = false,
  });
}
