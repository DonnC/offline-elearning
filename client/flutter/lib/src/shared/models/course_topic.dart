import 'index.dart';

/// per course topic
///
/// e.g Biology > Intro > ..(list of topic sections)..
class CourseTopic {
  final int? id;
  final String topic;
  final List<CourseContent>? courseContent;

  CourseTopic({
    this.id,
    required this.topic,
    this.courseContent = const [],
  });
}
