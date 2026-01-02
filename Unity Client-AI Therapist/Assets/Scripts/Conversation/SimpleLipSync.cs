using UnityEngine;

public class SimpleLipSync : MonoBehaviour
{
    [Header("Setup")]
    public SkinnedMeshRenderer faceMesh; // Drag 'U_Char_0' here
    public AudioSource audioSource;      // The speaker playing the voice

    [Header("Configuration")]
    public string mouthBlendShape = "3.kuchi"; // We will verify this name
    public float sensitivity = 100f;
    public float smoothSpeed = 20f;

    private int _blendShapeIndex = -1;
    private float _currentWeight;
    private float[] _samples = new float[256];

    void Start()
    {
        if (faceMesh == null)
        {
            Debug.LogError("SimpleLipSync: NO MESH ASSIGNED. Please assign U_Char_0.");
            enabled = false;
            return;
        }

        // AUTO-DISCOVERY: Find the index based on the name
        _blendShapeIndex = faceMesh.sharedMesh.GetBlendShapeIndex(mouthBlendShape);

        if (_blendShapeIndex == -1)
        {
            Debug.LogError($"[SimpleLipSync] ERROR: Could not find blendshape named '{mouthBlendShape}'.");
            Debug.Log("--- AVAILABLE BLENDSHAPES ---");
            for (int i = 0; i < faceMesh.sharedMesh.blendShapeCount; i++)
            {
                Debug.Log($"Name: {faceMesh.sharedMesh.GetBlendShapeName(i)}");
            }
            Debug.Log("-----------------------------");
            Debug.LogError("Check the Console logs above and copy the correct mouth name into the Inspector!");
        }
        else
        {
            Debug.Log($"[SimpleLipSync] SUCCESS: Linked to '{mouthBlendShape}'");
        }
    }

    void Update()
    {
        if (_blendShapeIndex == -1 || audioSource == null) return;

        // 1. Analyze Volume
        float volume = 0;
        if (audioSource.isPlaying)
        {
            audioSource.GetOutputData(_samples, 0);
            float sum = 0;
            foreach (float s in _samples) sum += s * s;
            volume = Mathf.Sqrt(sum / _samples.Length);
        }

        // 2. Animate
        float targetWeight = Mathf.Clamp(volume * sensitivity * 100f, 0f, 100f);
        _currentWeight = Mathf.Lerp(_currentWeight, targetWeight, Time.deltaTime * smoothSpeed);
        faceMesh.SetBlendShapeWeight(_blendShapeIndex, _currentWeight);
    }
}