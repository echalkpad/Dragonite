#include <opencv2/opencv.hpp>
#include <cstdlib>
using namespace std;
using namespace cv;

bool guard_range(float length, float point, float thresh) {
    assert(thresh<=1.0 && thresh>=0.0);
    return (point >= thresh*length && point <= length*(1-thresh));
}

int main(int argc, char* argv[]) {
    bool debug = false;
    debug = (argc >= 4);

    int max_count = 100;
    Mat image_prev = imread(argv[1], CV_LOAD_IMAGE_GRAYSCALE);
    Mat image_next = imread(argv[2], CV_LOAD_IMAGE_GRAYSCALE);
//    double angle = atof(argv[3]);

    Mat display_prev, display_next;
    cvtColor(image_prev, display_prev, CV_GRAY2RGB);
    cvtColor(image_next, display_next, CV_GRAY2RGB);

    vector<Point2f> features_prev, features_next;

    goodFeaturesToTrack(image_next, // the image
                        features_prev,   // the output detected features
                        max_count,  // the maximum number of features
                        0.01,
                        5);     // min distance between two features
// Tracker is initialised and initial features are stored in features_next
// Now iterate through rest of images
    // Find position of feature in new image
    Mat status, err;

    calcOpticalFlowPyrLK(
        image_prev, image_next, // 2 consecutive images
        features_prev, // input point positions in first im
        features_next, // output point positions in the 2nd
        status,    // tracking success
        err);      // tracking error

    int i, j;
    for (i=0, j=0; i<features_prev.size() && j<features_next.size(); i++, j++) {
        if (status.at<unsigned char>(i, 0) == 1) {
            float dx = features_next[i].x - features_prev[i].x;
            float dy = features_next[i].y - features_prev[i].y;

            // Guard horizontal
            if (abs(dy/(dx+0.0001))>0.5773)
                continue;

            // Guard box
            if (guard_range(display_next.cols, features_next[i].x, 0.15) &&
                guard_range(display_next.rows, features_next[i].y, 0.1))
                continue;

            cout << "[" << features_prev[i] << ", " << features_next[i] << "]" << endl;
            if (debug) {
                line(display_prev, features_prev[i], features_next[i], Scalar(0, 255, 0));
                line(display_next, features_prev[i], features_next[i], Scalar(0, 255, 0));
                circle(display_prev, features_prev[i], 2, Scalar(0, 255, 255));
                circle(display_next, features_next[i], 2, Scalar(0, 255, 255));
            }
        }
    }

    if (debug) {
        namedWindow("image1");
        namedWindow("image2");
        imshow("image1", display_prev);
        imshow("image2", display_next);

        while (waitKey(0) != 32);
    }

    return 0;
}
