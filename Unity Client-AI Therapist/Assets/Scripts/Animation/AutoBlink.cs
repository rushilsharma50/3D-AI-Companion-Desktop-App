using UnityEngine;
using System.Collections;

public class AutoBlink : MonoBehaviour
{
    public SkinnedMeshRenderer faceMesh;
    public string blinkBlendShape = "24.まばたき"; // The name from your screenshot
    public float blinkDuration = 0.1f;    // Fast blink
    public float minTime = 2f;            // Minimum time between blinks
    public float maxTime = 6f;            // Maximum time between blinks

    private int _blendShapeIndex;

    void Start()
    {
        if (faceMesh == null)
        {
            Debug.LogError("Assign the Face Mesh!");
            enabled = false;
            return;
        }

        _blendShapeIndex = faceMesh.sharedMesh.GetBlendShapeIndex(blinkBlendShape);
        
        if (_blendShapeIndex == -1) 
            Debug.LogError($"Could not find Blink shape: {blinkBlendShape}");
        else 
            StartCoroutine(BlinkRoutine());
    }

    IEnumerator BlinkRoutine()
    {
        while (true)
        {
            // 1. Wait for random time
            yield return new WaitForSeconds(Random.Range(minTime, maxTime));

            // 2. Close Eyes
            float timer = 0f;
            while (timer < blinkDuration)
            {
                timer += Time.deltaTime;
                float weight = Mathf.Lerp(0, 100, timer / blinkDuration);
                faceMesh.SetBlendShapeWeight(_blendShapeIndex, weight);
                yield return null;
            }

            // 3. Open Eyes
            timer = 0f;
            while (timer < blinkDuration)
            {
                timer += Time.deltaTime;
                float weight = Mathf.Lerp(100, 0, timer / blinkDuration);
                faceMesh.SetBlendShapeWeight(_blendShapeIndex, weight);
                yield return null;
            }
        }
    }
}