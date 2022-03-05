// mock service implementation
import 'package:client/src/shared/models/course.dart';
import 'package:client/src/shared/models/course_content.dart';
import 'package:client/src/shared/models/course_topic.dart';

import 'api_service.dart';

class FakeApiServiceImpl implements ApiService {
  @override
  Future addCourse(Course? course) {
    // TODO: implement addCourse
    throw UnimplementedError();
  }

  @override
  Future addCourseTopic(CourseTopic? courseTopic) {
    // TODO: implement addCourseTopic
    throw UnimplementedError();
  }

  @override
  Future addCourseTopicContent(CourseContent? content) {
    // TODO: implement addCourseTopicContent
    throw UnimplementedError();
  }

  @override
  Future getAllCourseTopics(int? courseId) {
    // TODO: implement getAllCourseTopics
    throw UnimplementedError();
  }

  @override
  Future<List<Course>?> getAllCourses(String? grade) async {
    // TODO: implement getAllCourses
    await Future.delayed(const Duration(seconds: 3));

    return [
      Course(name: 'Biology', description: ''),
    ];
  }

  @override
  Future getCourseById(int id) {
    // TODO: implement getCourseById
    throw UnimplementedError();
  }

  @override
  Future getCourseTopicContent(int topicId) {
    // TODO: implement getCourseTopicContent
    throw UnimplementedError();
  }
}
