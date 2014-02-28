/**
 * @file SURF_FlannMatcher
 * @brief SURF detector + descriptor + FLANN Matcher
 * @author A. Huaman
 */

#include <cstdio>
#include <iostream>
#include <cmath>
#include "opencv2/core/core.hpp"
#include "opencv2/features2d/features2d.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/nonfree/features2d.hpp"
using namespace std;
using namespace cv;

/**
 * @function main
 * @brief Main function
 */
int main( int argc, char** argv )
{
    bool debug = false;

    if (argc >= 4) {
        debug = true;
    }
    Mat leftImageGrey = imread( argv[1], CV_LOAD_IMAGE_GRAYSCALE );
    Mat rightImageGrey = imread( argv[2], CV_LOAD_IMAGE_GRAYSCALE );

    Ptr<FeatureDetector> detector;
    vector<KeyPoint> keypoints_1, keypoints_2;
    Mat descriptors_1, descriptors_2;

    detector = new DynamicAdaptedFeatureDetector(new FastAdjuster(10,true), 5000,
                                                 10000, 10);
    detector->detect(leftImageGrey, keypoints_1);
    detector->detect(rightImageGrey, keypoints_2);

    Ptr<DescriptorExtractor> extractor = DescriptorExtractor::create("SIFT");
    extractor->compute( leftImageGrey, keypoints_1, descriptors_1 );
    extractor->compute( rightImageGrey, keypoints_2, descriptors_2 );

    vector< vector<DMatch> > matches;
    Ptr<DescriptorMatcher> matcher = DescriptorMatcher::create("BruteForce");
    matcher->knnMatch( descriptors_1, descriptors_2, matches, 500 );

   //look whether the match is inside a defined area of the image
   //only 25% of maximum of possible distance
    double tresholdDist = 0.05 * sqrt(double(leftImageGrey.size().height *
                                             leftImageGrey.size().height +
                                             leftImageGrey.size().width *
                                             leftImageGrey.size().width));

    vector< DMatch > good_matches2;
    good_matches2.reserve(matches.size());

    for (size_t i = 0; i < matches.size(); ++i) {
        for (int j = 0; j < matches[i].size(); j++) {
            Point2f from = keypoints_1[matches[i][j].queryIdx].pt;
            Point2f to = keypoints_2[matches[i][j].trainIdx].pt;

            //calculate local distance for each possible match
            double dist = sqrt((from.x - to.x) * (from.x - to.x) +
                               (from.y - to.y) * (from.y - to.y));

            // save as best match if local distance is in specified area and on same
            // height
            if (dist < tresholdDist && abs(from.y-to.y)<5) {
                good_matches2.push_back(matches[i][j]);
                j = matches[i].size();
            }
        }
    }

    cout << good_matches2.size() << " " << keypoints_1.size() << " " << keypoints_2.size() << endl;

    if (debug) {
        Mat img_matches;
        drawMatches(leftImageGrey, keypoints_1, rightImageGrey, keypoints_2,
                    good_matches2, img_matches, Scalar::all(-1), Scalar::all(-1),
                    vector<char>(), DrawMatchesFlags::NOT_DRAW_SINGLE_POINTS);

        //-- Show detected matches

        imshow("Good Matches", img_matches);

        // for( int i = 0; i < (int)good_matches.size(); i++ ) {
        //     printf( "-- Good Match [%d] Keypoint 1: %d  -- Keypoint 2: %d  \n",
        //             i, good_matches[i].queryIdx, good_matches[i].trainIdx ); }

        waitKey(0);
    }

    return 0;
}
