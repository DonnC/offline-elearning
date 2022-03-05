import 'index.dart';

/// main course | subject
///
/// e.g Maths | Biology
class Course {
  final int? id;
  final DateTime? createdOn;
  final String? image;
  final String name;
  final String? title;
  final String description;
  final List<Content> content;

  Course({
    this.id,
    this.createdOn,
    this.image,
    required this.name,
    this.title,
    required this.description,
    this.content = const [],
  });
}
