import 'dart:ui';
import 'dart:math' as math;

class AppColors {
  static const Color greyishBgColor = Color(0xFFF4F5F6);
  static const Color greyBgColor = Color(0xFFE2E6E9);
  static const Color whiteColor = Color(0xFFFFFFFF);
  static const Color buttonBgColor = Color(0xFF2490EF);
  static const Color greenishColor = Color(0xFF68D391);

  /// course background color swatches
  static final List<Color> bgColorSwatches = [
    const Color(0xFFFDF9F2),
    const Color(0xFFFFECCA),
    const Color(0xFFFEF4E2),
    const Color(0xFFF2F2FD),
    const Color(0xFFEBF4FC),
  ];

  static Color getRandomColor() {
    var g = math.Random().nextInt(bgColorSwatches.length);

    return bgColorSwatches[g];
  }
}
