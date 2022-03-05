import 'dart_server.dart';

class MyConfiguration extends Configuration {
  MyConfiguration(String configPath) : super.fromFile(File(configPath));

  DatabaseConfiguration? database;
}
