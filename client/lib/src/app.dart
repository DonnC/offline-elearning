import 'package:client/src/constants/index.dart';
import 'package:client/src/shared/screens/shared_grade_selector_view.dart';
import 'package:client/src/shared/screens/shared_home_view.dart';
import 'package:flutter/material.dart';

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
        switch (settings.name) {
          case sharedGradeSelector:
            return MaterialPageRoute(builder: (_) => const SharedGradeSelectorView());

          // case detailScreen:
          // return MaterialPageRoute(builder: (_) => DetailScreen(arguments: settings.arguments as Map<String, dynamic>));

          default:
            return MaterialPageRoute(builder: (_) => const SharedHomeView());
        }
      },
    );
  }
}
