#define BOOST_TEST_MODULE FCL_SIMPLE
#include <boost/test/included/unit_test.hpp>

#include <hpp/fcl/internal/intersect.h>
#include <hpp/fcl/collision.h>
#include <hpp/fcl/BVH/BVH_model.h>
#include "fcl_resources/config.h"
#include <sstream>

using namespace hpp::fcl;

static FCL_REAL epsilon = 1e-6;

static bool approx(FCL_REAL x, FCL_REAL y) { return std::abs(x - y) < epsilon; }

BOOST_AUTO_TEST_CASE(projection_test_line) {
  Vec3f v1(0, 0, 0);
  Vec3f v2(2, 0, 0);

  Vec3f p(1, 0, 0);
  Project::ProjectResult res = Project::projectLine(v1, v2, p);
  BOOST_CHECK(res.encode == 3);
  BOOST_CHECK(approx(res.sqr_distance, 0));
  BOOST_CHECK(approx(res.parameterization[0], 0.5));
  BOOST_CHECK(approx(res.parameterization[1], 0.5));

  p = Vec3f(-1, 0, 0);
  res = Project::projectLine(v1, v2, p);
  BOOST_CHECK(res.encode == 1);
  BOOST_CHECK(approx(res.sqr_distance, 1));
  BOOST_CHECK(approx(res.parameterization[0], 1));
  BOOST_CHECK(approx(res.parameterization[1], 0));

  p = Vec3f(3, 0, 0);
  res = Project::projectLine(v1, v2, p);
  BOOST_CHECK(res.encode == 2);
  BOOST_CHECK(approx(res.sqr_distance, 1));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 1));
}

BOOST_AUTO_TEST_CASE(projection_test_triangle) {
  Vec3f v1(0, 0, 1);
  Vec3f v2(0, 1, 0);
  Vec3f v3(1, 0, 0);

  Vec3f p(1, 1, 1);
  Project::ProjectResult res = Project::projectTriangle(v1, v2, v3, p);
  BOOST_CHECK(res.encode == 7);
  BOOST_CHECK(approx(res.sqr_distance, 4 / 3.0));
  BOOST_CHECK(approx(res.parameterization[0], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[1], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[2], 1 / 3.0));

  p = Vec3f(0, 0, 1.5);
  res = Project::projectTriangle(v1, v2, v3, p);
  BOOST_CHECK(res.encode == 1);
  BOOST_CHECK(approx(res.sqr_distance, 0.25));
  BOOST_CHECK(approx(res.parameterization[0], 1));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 0));

  p = Vec3f(1.5, 0, 0);
  res = Project::projectTriangle(v1, v2, v3, p);
  BOOST_CHECK(res.encode == 4);
  BOOST_CHECK(approx(res.sqr_distance, 0.25));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 1));

  p = Vec3f(0, 1.5, 0);
  res = Project::projectTriangle(v1, v2, v3, p);
  BOOST_CHECK(res.encode == 2);
  BOOST_CHECK(approx(res.sqr_distance, 0.25));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 1));
  BOOST_CHECK(approx(res.parameterization[2], 0));

  p = Vec3f(1, 1, 0);
  res = Project::projectTriangle(v1, v2, v3, p);
  BOOST_CHECK(res.encode == 6);
  BOOST_CHECK(approx(res.sqr_distance, 0.5));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 0.5));
  BOOST_CHECK(approx(res.parameterization[2], 0.5));

  p = Vec3f(1, 0, 1);
  res = Project::projectTriangle(v1, v2, v3, p);
  BOOST_CHECK(res.encode == 5);
  BOOST_CHECK(approx(res.sqr_distance, 0.5));
  BOOST_CHECK(approx(res.parameterization[0], 0.5));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 0.5));

  p = Vec3f(0, 1, 1);
  res = Project::projectTriangle(v1, v2, v3, p);
  BOOST_CHECK(res.encode == 3);
  BOOST_CHECK(approx(res.sqr_distance, 0.5));
  BOOST_CHECK(approx(res.parameterization[0], 0.5));
  BOOST_CHECK(approx(res.parameterization[1], 0.5));
  BOOST_CHECK(approx(res.parameterization[2], 0));
}

BOOST_AUTO_TEST_CASE(projection_test_tetrahedron) {
  Vec3f v1(0, 0, 1);
  Vec3f v2(0, 1, 0);
  Vec3f v3(1, 0, 0);
  Vec3f v4(1, 1, 1);

  Vec3f p(0.5, 0.5, 0.5);
  Project::ProjectResult res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 15);
  BOOST_CHECK(approx(res.sqr_distance, 0));
  BOOST_CHECK(approx(res.parameterization[0], 0.25));
  BOOST_CHECK(approx(res.parameterization[1], 0.25));
  BOOST_CHECK(approx(res.parameterization[2], 0.25));
  BOOST_CHECK(approx(res.parameterization[3], 0.25));

  p = Vec3f(0, 0, 0);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 7);
  BOOST_CHECK(approx(res.sqr_distance, 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[0], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[1], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[2], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[3], 0));

  p = Vec3f(0, 1, 1);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 11);
  BOOST_CHECK(approx(res.sqr_distance, 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[0], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[1], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[2], 0));
  BOOST_CHECK(approx(res.parameterization[3], 1 / 3.0));

  p = Vec3f(1, 1, 0);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 14);
  BOOST_CHECK(approx(res.sqr_distance, 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[2], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[3], 1 / 3.0));

  p = Vec3f(1, 0, 1);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 13);
  BOOST_CHECK(approx(res.sqr_distance, 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[0], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 1 / 3.0));
  BOOST_CHECK(approx(res.parameterization[3], 1 / 3.0));

  p = Vec3f(1.5, 1.5, 1.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 8);
  BOOST_CHECK(approx(res.sqr_distance, 0.75));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 0));
  BOOST_CHECK(approx(res.parameterization[3], 1));

  p = Vec3f(1.5, -0.5, -0.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 4);
  BOOST_CHECK(approx(res.sqr_distance, 0.75));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 1));
  BOOST_CHECK(approx(res.parameterization[3], 0));

  p = Vec3f(-0.5, -0.5, 1.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 1);
  BOOST_CHECK(approx(res.sqr_distance, 0.75));
  BOOST_CHECK(approx(res.parameterization[0], 1));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 0));
  BOOST_CHECK(approx(res.parameterization[3], 0));

  p = Vec3f(-0.5, 1.5, -0.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 2);
  BOOST_CHECK(approx(res.sqr_distance, 0.75));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 1));
  BOOST_CHECK(approx(res.parameterization[2], 0));
  BOOST_CHECK(approx(res.parameterization[3], 0));

  p = Vec3f(0.5, -0.5, 0.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 5);
  BOOST_CHECK(approx(res.sqr_distance, 0.25));
  BOOST_CHECK(approx(res.parameterization[0], 0.5));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 0.5));
  BOOST_CHECK(approx(res.parameterization[3], 0));

  p = Vec3f(0.5, 1.5, 0.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 10);
  BOOST_CHECK(approx(res.sqr_distance, 0.25));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 0.5));
  BOOST_CHECK(approx(res.parameterization[2], 0));
  BOOST_CHECK(approx(res.parameterization[3], 0.5));

  p = Vec3f(1.5, 0.5, 0.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 12);
  BOOST_CHECK(approx(res.sqr_distance, 0.25));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 0.5));
  BOOST_CHECK(approx(res.parameterization[3], 0.5));

  p = Vec3f(-0.5, 0.5, 0.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 3);
  BOOST_CHECK(approx(res.sqr_distance, 0.25));
  BOOST_CHECK(approx(res.parameterization[0], 0.5));
  BOOST_CHECK(approx(res.parameterization[1], 0.5));
  BOOST_CHECK(approx(res.parameterization[2], 0));
  BOOST_CHECK(approx(res.parameterization[3], 0));

  p = Vec3f(0.5, 0.5, 1.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 9);
  BOOST_CHECK(approx(res.sqr_distance, 0.25));
  BOOST_CHECK(approx(res.parameterization[0], 0.5));
  BOOST_CHECK(approx(res.parameterization[1], 0));
  BOOST_CHECK(approx(res.parameterization[2], 0));
  BOOST_CHECK(approx(res.parameterization[3], 0.5));

  p = Vec3f(0.5, 0.5, -0.5);
  res = Project::projectTetrahedra(v1, v2, v3, v4, p);
  BOOST_CHECK(res.encode == 6);
  BOOST_CHECK(approx(res.sqr_distance, 0.25));
  BOOST_CHECK(approx(res.parameterization[0], 0));
  BOOST_CHECK(approx(res.parameterization[1], 0.5));
  BOOST_CHECK(approx(res.parameterization[2], 0.5));
  BOOST_CHECK(approx(res.parameterization[3], 0));
}
