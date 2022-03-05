import 'package:client/src/shared/models/index.dart';

abstract class ApiService {
  /// get all courses by grade or get all
  Future getAllCourses(String? grade) async {}

  Future getCourseById(int id) async {}

  Future getAllCourseTopics(int? courseId) async {}

  Future getCourseTopicContent(int topicId) async {}

  Future addCourse(Course? course) async {}

  Future addCourseTopic(CourseTopic? courseTopic) async {}

  Future addCourseTopicContent(CourseContent? content) async {}
}
