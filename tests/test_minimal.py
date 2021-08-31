"""
test_minimal.py
--------------

Test things that should work with a *minimal* trimesh install.


"""
import os

import unittest
import trimesh

# the path of the current directory
_pwd = os.path.dirname(
    os.path.abspath(os.path.expanduser(__file__)))
# the absolute path for our reference models
_mwd = os.path.abspath(
    os.path.join(_pwd, '..', 'models'))


def get_mesh(file_name, **kwargs):
    return trimesh.load(os.path.join(_mwd, file_name),
                        **kwargs)


class MinimalTest(unittest.TestCase):

    def test_load(self):
        # kinds of files we should be able to
        # load even with a minimal install
        kinds = 'stl ply obj off gltf glb'.split()

        for file_name in os.listdir(_mwd):
            ext = os.path.splitext(file_name)[-1].lower()[1:]
            if ext not in kinds:
                continue

            print(file_name)
            m = get_mesh(file_name)
            if isinstance(m, trimesh.Trimesh):
                assert len(m.face_adjacency.shape) == 2
                assert len(m.vertices.shape) == 2

                # make sure hash changes
                initial = m._data.fast_hash()
                m.vertices[:, 0] += 1.0
                assert m._data.fast_hash() != initial


if __name__ == '__main__':
    trimesh.util.attach_to_log()
    unittest.main()
