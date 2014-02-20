#include "opencv2/opencv.hpp"
using namespace std;
using namespace cv;

RNG rng(12345);

int main(int argc, char* argv[]) {
    Mat edge;
    Mat image = imread(argv[1], CV_LOAD_IMAGE_GRAYSCALE);
    Mat out;
    threshold(image, out, 230, 255, THRESH_BINARY);

    Mat element = getStructuringElement(MORPH_RECT,
                                        Size(20, 20),
                                        Point(3, 3));
    dilate(out, out, element );
    element = getStructuringElement(MORPH_RECT,
                                    Size(40, 40),
                                    Point(3, 3));
    erode(out, out, element);
    element = getStructuringElement(MORPH_RECT,
                                    Size(20, 20),
                                    Point(3, 3));
    dilate(out, out, element);


    Canny(out, edge, 10, 10);

    vector<vector<Point>> contours;
    vector<Vec4i> hierarchy;
    Mat edges = edge.clone();
    Mat outmat = Mat::zeros(edges.size(), CV_8UC3);
    findContours(edges, contours, hierarchy, CV_RETR_LIST, CV_CHAIN_APPROX_NONE, Point(0, 0) );

    double max = 0;
    vector<Point> ct;
    for (auto c:contours) {
        double a = contourArea(c);
        if (a > max) {
            max = a;
            ct = c;
        }
    }

    for (int i=0; i<ct.size()-1; i++) {
        Point p1 = ct[i];
        Point p2 = ct[i+1];
        line(outmat, p1, p2, Scalar(255, 255, 0));
    }
    // for (auto c:contours) {
    //     double area = contourArea(c, true);
    //     cout << "Area: " << area << endl;
    // }
    namedWindow("win");
    imshow("win", outmat);

    while (waitKey(20) != 32);
    return 0;
}
