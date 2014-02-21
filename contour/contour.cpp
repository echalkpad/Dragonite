#include "opencv2/opencv.hpp"
#include <map>
#include <cmath>
using namespace std;
using namespace cv;

RNG rng(12345);
int step = 30;
int required = 2;

double contour_length(vector<Point>& v) {
    double sum = 0.0;
    for (int i=0; i<v.size()-1; i++) {
        double dx = abs(v[i+1].x - v[i].x);
        double dy = abs(v[i+1].y - v[i].y);
        sum += (dx + dy);
    }
    return sum;
}

bool is_aligned(double x1, double y1, double x2, double y2) {
    return (abs(x1 * x2 + y1 * y2) <= 0.01);
}

Point primary_vec(vector<Point>& v) {
    double cur = 0.0;
    bool finished = false;

    step = v.size() - 1;
    while (!finished) {
        int aligned = 0;
        step -= 1;
        for (int deg=0; deg<90; deg++) {
            double rad = deg * M_PI / 180.0;
            double vx = cos(rad);
            double vy = sin(rad);

            int cnt = 0;
            int l = 0;

            for (int i=0; i<v.size()-step; i+=step) {
                double cx = v[i+step].x - v[i].x;
                double cy = v[i+step].y - v[i].y;

                if (is_aligned(cx, cy, vx, vy) && abs(cx)+abs(cy)>=4) {
                    cnt += 1;
                    l += (abs(cx)+ abs(cy));
                }

            }

            if (l > aligned) {
                aligned = l;
                cur = deg;
                cout << "Deg: " << deg << " Aligned: " << aligned <<  " cnt: " << cnt << " step: " << step << endl;
                if (cnt >= required) {
                    cout << "Required: " << required << " Aligned: " << cnt << endl;
                    finished = true;
                }
            }
        }

    }

    return Point(cur, cur+90.0);
}

void line_on_angle(Mat& m, double deg, int l, Scalar color) {
    int dx = l * cos(M_PI / 180.0 * deg);
    int dy = l * sin(M_PI / 180.0 * deg);

    int cx = m.cols / 2;
    int cy = m.rows / 2;

    line(m, Point(cx, cy), Point(cx+dx, cy+dy), color);
}

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
    Mat outmat = Mat::zeros(edge.size(), CV_8UC3);
    cvtColor(image, outmat, CV_GRAY2RGB);
    findContours(edges, contours, hierarchy, CV_RETR_LIST, CV_CHAIN_APPROX_TC89_L1, Point(0, 0) );

    double max = 0;
    vector<Point> ct;
    for (auto c:contours) {
        double a = contour_length(c);
        if (a > max) {
            max = a;
            ct = c;
        }
    }

    Point p = primary_vec(ct);
    cout << "Step: " << step << " Primary: " << p.x << " " << p.y << endl;

    for (int i=0; i<ct.size()-step; i+=step) {
        Point p1 = ct[i];
        Point p2 = ct[i+step];
        line(outmat, p1, p2, Scalar(255, 255, 0));
    }

    line_on_angle(outmat, p.x, 50, Scalar(0, 0, 255));
    line_on_angle(outmat, p.y, 50, Scalar(255, 0, 0));

    // for (auto c:contours) {
    //     double area = contourArea(c, true);
    //     cout << "Area: " << area << endl;
    // }
    namedWindow("win");
    imshow("win", outmat);

    while (waitKey(20) != 32);
    return 0;
}
