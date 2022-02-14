import 'index.dart';

/// main grade or level
///
/// e.g Form4
class Grade {
  final int? id;
  final String name;
  final String? description;
  final List<Course> course;
  final List<Teacher>? teachers;

  Grade({
    this.id,
    required this.name,
    this.description,
    required this.course,
    this.teachers,
  });
  // TODO Add associated media files too
}
