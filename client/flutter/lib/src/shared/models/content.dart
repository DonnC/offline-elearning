import 'index.dart';

/// main content section
///
/// can be main header or topic
///
/// e.g Introduction -> for course / Subject Maths
class Content {
  final int? id;
  final DateTime createdOn;
  final String title;
  final String? description;
  final List<CourseTopic>? topics;

  Content({
    this.id,
    required this.createdOn,
    required this.title,
    this.description,
    this.topics = const [],
  });
}
