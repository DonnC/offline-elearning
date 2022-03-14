import 'package:client/src/constants/index.dart';
import 'package:client/src/shared/screens/course_content_view.dart';
import 'package:client/src/shared/screens/shared_form_courses_view.dart';
import 'package:client/src/shared/screens/shared_grade_selector_view.dart';
//import 'package:client/src/shared/screens/shared_home_view.dart';
import 'package:flutter/material.dart';

import 'shared/screens/zefyr_editor.dart';
import 'utils/app_theme.dart';

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Offline eLearning Sys',
      theme: theme,
      initialRoute: sharedHomeScreen,
      onGenerateRoute: (settings) {
        var args = settings.arguments as Map<String, dynamic>?;

        switch (settings.name) {
          case sharedGradeSelector:
            return MaterialPageRoute(
                builder: (_) => const SharedGradeSelectorView());

          case sharedPerFormScreen:
            return MaterialPageRoute(
                builder: (_) => SharedFormCoursesView(args: args));

          case courseContentScreen:
            return MaterialPageRoute(
                builder: (_) => CourseContentView(args: args));

          default:
            // return MaterialPageRoute(builder: (_) => const SharedHomeView());
            return MaterialPageRoute(builder: (_) => const EditorPage());
        }
      },
    );
  }
}
