using UnityEngine;

public class HeadTracking : MonoBehaviour
{
    [Header("Setup")]
    public Transform headBone;       // Drag Chisa's Head bone here
    public Transform target;         // Drag your Main Camera here
    
    [Header("Anatomy Settings")]
    public float sensitivity = 5.0f; // How fast she turns
    public float maxAngle = 60.0f;   // Limit neck rotation (prevents Exorcist moments)
    public Vector3 rotationOffset = new Vector3(0, 90, -90); // ADJUST THIS if she looks sideways!

    private Quaternion _initialRotation;

    void Start()
    {
        if (!headBone || !target)
        {
            Debug.LogError("HeadTracking: Missing Head Bone or Target Camera!");
            enabled = false;
            return;
        }
        // Store the comfortable "forward" rotation relative to her body
        _initialRotation = headBone.localRotation;
    }

    // LateUpdate runs AFTER animation. 
    // This allows the Idle animation to play, and THEN we rotate the head on top of it.
    void LateUpdate()
    {
        // 1. Get direction to user
        Vector3 directionToTarget = target.position - headBone.position;

        // 2. Calculate the rotation needed to look at user
        Quaternion targetRotation = Quaternion.LookRotation(directionToTarget);

        // 3. Apply the corrective offset (3D models often have weird bone axis)
        // If she looks 90 degrees wrong, change rotationOffset in Inspector
        targetRotation *= Quaternion.Euler(rotationOffset);

        // 4. CLAMP: Limit the angle so she doesn't break her neck
        // We calculate the angle between her body's forward and the target
        float angle = Quaternion.Angle(transform.rotation * _initialRotation, targetRotation);
        
        if (angle > maxAngle)
        {
            // If the user is too far sideways, just look as far as possible
            targetRotation = Quaternion.RotateTowards(transform.rotation * _initialRotation, targetRotation, maxAngle);
        }

        // 5. SMOOTH: Slerp allows for natural, non-robotic movement
        headBone.rotation = Quaternion.Slerp(headBone.rotation, targetRotation, Time.deltaTime * sensitivity);
    }
}