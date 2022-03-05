/// past exam paper, pdf
/// 
/// TODO might not be necessary
class PastPaper {
  final int? id;
  final String year;
  final String name;
  final String url; // file path where paper is
  PastPaper({
    this.id,
    required this.year,
    required this.name,
    required this.url,
  });
}
